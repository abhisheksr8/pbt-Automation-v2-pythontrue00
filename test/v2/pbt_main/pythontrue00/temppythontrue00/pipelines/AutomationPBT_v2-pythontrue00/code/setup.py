from setuptools import setup, find_packages
setup(
    name = 'AutomationPBT_v2-pythontrue00',
    version = '1.0',
    packages = (
      find_packages(include = ('automationpbt_v2pythontrue00*', ))
      + ['prophecy_config_instances.automationpbt_v2pythontrue00']
    ),
    package_dir = {'prophecy_config_instances.automationpbt_v2pythontrue00' : 'configs/resources/automationpbt_v2pythontrue00'},
    package_data = {'prophecy_config_instances.automationpbt_v2pythontrue00' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.33'],
    entry_points = {
'console_scripts' : [
'main = automationpbt_v2pythontrue00.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
