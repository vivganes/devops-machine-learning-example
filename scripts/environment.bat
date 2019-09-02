CALL conda.bat activate mybuild
echo %CONDA_PREFIX%
pip install -r requirements.txt
pip install -r requirements/dev.txt
