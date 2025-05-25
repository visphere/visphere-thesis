import os
import argparse
import shutil
import subprocess
from pathlib import Path

script_dir = Path(__file__).parent.resolve()

def compile_latex_single_run(tex_file_dir, build_dir, quiet):
  command = [
    "lualatex",
    "-shell-escape",
    "-synctex=1",
    "-file-line-error",
    f"-output-directory={build_dir}",
  ]
  if quiet:
    command.append("-interaction=batchmode")
  command.append("main.tex")
  subprocess.run(command, cwd=tex_file_dir, check=True, timeout=300)

def remove_temp_files(build_dir):
  for file in Path(build_dir).rglob("*"):
    if not file.is_file() or file.suffix.lower() == ".pdf":
      continue
    try:
      file.unlink()
    except Exception as _:
      pass

def compile_latex(quiet):
  if quiet:
    print("uruchamiam cichy tryb kompilacji LaTeX")

  build_dir = os.path.join(script_dir, "build")
  tex_file_dir = os.path.join(script_dir)

  shutil.rmtree(build_dir, ignore_errors=True)
  Path(build_dir).mkdir(parents=True, exist_ok=True)
  print(f"usuwam poprzednie kompilacje LaTeX z katalogu {build_dir}")

  print("\nrozpoczynam kompilację LaTeX\n")
  compile_latex_single_run(tex_file_dir, build_dir, quiet)

  print("\nrozpoczynam ponowną kompilację LaTeX (rozwiązanie referencji)\n")
  compile_latex_single_run(tex_file_dir, build_dir, quiet)

  print("\nusuwam pliki tymczasowe kompilacji")
  remove_temp_files(build_dir)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--quiet", action="store_true", help="Tryb cichy (bez logów)")

  args = parser.parse_args()

  compile_latex(args.quiet)
  print("kompilacja zakończona")
