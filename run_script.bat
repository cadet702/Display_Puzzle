@ECHO OFF
color 2
echo Ready to launch script
Set "script_path=C:\Users\%USERNAME%\Desktop\Display_Puzzle"
Set "python_path=C:\Users\%USERNAME%\Anaconda3\envs\Display_Env_2"
:: pause

cd "%script_path%"
"%python_path%\python.exe" "%script_path%\sprites.py" "%script_path%\test_cases\random_inputs.txt" "compute_sprite_positions"
echo Process complete!
pause