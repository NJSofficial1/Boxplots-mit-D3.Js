import os
import json

def read_json(json_path: str)-> list:
    """
    reads data from .json file and extracts data of a group. Therefore, you must add ['<group name>'] just after
    data = json.load(open(f))
    :param json_path: dynamic path to json file

    returns: extracted list of dictionaries: each dictionary contains group name like ("normalverteilt" or "ausreisser")
             and its data

    raises:
            FileNotFoundError: if file is not existing
            KeyError: if key name does not exists in the file
    """
    with open(json_path, "r") as f:
        data = json.load(f)['gruppen']
    return data

def read_html_template(html_path: str)-> str:
    """
    reads .html file as a template to inject data into later on
    :param html_path: dynamic path to html file
    returns:    content of .html template as string
    raises:     FileNotFoundError: if file is not existing
    """
    with open(html_path, "r", encoding="utf-8") as f:
        html_template = f.read()
    return html_template

def read_config_js(config_path: str)-> str:
    """
    reads config.js to inject configuration into html-template
    :param config_path: dynamic path to config.js file
    returns:    content of config.js as string to inject later on
    """
    with open(config_path, "r", encoding="utf-8") as f:
        config_template = f.read()
    return config_template

def inject_data_into_html(data: list, html_template: str, config_template: str) -> str:
    """
    injects data into html template by transforming data list to a string
    :param data: list of data to inject
    :param html_template: html template to inject data and config in
    :param config_template: config variables in js-script to be injected
    returns: final html file, which can be rendered in browser and shows the final plot
    """

    injected_content = f"""
    <script>
        const chartData = {json.dumps(data)};
        {config_template}
    </script>
    """
    # insert config directly after opening <head> tag,
    # so that it is loaded at the right position in html code
    return html_template.replace("<head>", f"<head>\n{injected_content}")

def generate_boxplot(json_path: str, html_path: str, config_path: str) -> str:
    """
    function to orchestrate boxplot generation by calling auxiliary functions
    :param json_path: dynamic path to json file
    :param html_path: dynamic path to html file
    :returns: final html file, which can be rendered in browser and shows the final plot
    """
    data_groups = read_json(json_path)
    config_template = read_config_js(config_path)
    html_final = read_html_template(html_path)

    return inject_data_into_html(data_groups, html_final, config_template)