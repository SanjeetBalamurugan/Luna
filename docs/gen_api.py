from pathlib import Path
import mkdocs_gen_files

src_dir = Path("src/luna")
docs_dir = Path("reference")

for path in src_dir.rglob("*.py"):
    module_path = path.relative_to("src").with_suffix("")
    doc_path = docs_dir / module_path.with_suffix(".md")
    full_module_name = ".".join(module_path.parts)

    with mkdocs_gen_files.open(doc_path, "w") as f:
        print(f"# `{full_module_name}`", file=f)
        print(f"\n::: {full_module_name}", file=f)

    mkdocs_gen_files.set_edit_path(doc_path, path)
