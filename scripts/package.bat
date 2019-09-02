CALL conda activate.bat mybuild
echo "hello" %CONDA_PREFIX%
python setup.py bdist_wheel
