@echo off
cd ..
setlocal
FOR /F "tokens=*" %%i in ('type .env') do SET %%i
python -m bot.main
endlocal
pause