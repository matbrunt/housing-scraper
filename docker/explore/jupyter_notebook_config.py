import io
import os
import re

from notebook.utils import to_api_path

c = get_config()

_markdown_exporter = None
_script_exporter = None

def save_as_markdown_and_script_post_save(model, os_path, contents_manager, **kwargs):
    from nbconvert.exporters.markdown import MarkdownExporter
    from nbconvert.exporters.script import ScriptExporter

    if model['type'] != 'notebook':
        return
    log = contents_manager.log
    base, ext = os.path.splitext(os_path)
    
    from subprocess import call
    markdown_cmd = "jupyter nbconvert --to markdown"
    call(markdown_cmd.split() + [os_path])
    
    global _script_exporter
    if _script_exporter is None:
        _script_exporter = ScriptExporter(parent=contents_manager)
    
    script, script_resources = _script_exporter.from_filename(os_path)
    script_fname = base + script_resources.get('output_extension', '.py')
    log.info("Saving script /%s", to_api_path(script_fname, contents_manager.root_dir))
    
    with io.open(script_fname, 'w', encoding='utf-8') as f:
        script = re.sub(r"# In\[(\d+| )\]:\n", "", script)
        f.write(script)

c.FileContentsManager.post_save_hook = save_as_markdown_and_script_post_save