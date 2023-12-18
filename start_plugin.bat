@echo off

@REM 检查端口是否被占用
netstat -ano | findstr "12300" > nul
if %errorlevel% equ 0 (
    @REM 端口被占用,找到占用端口的进程并杀掉
    for /f "tokens=5" %%i in ('netstat -ano ^| findstr "12300"') do (
        taskkill /f /pid %%i
    )
)

@REM 切换到代码目录 
cd /d preview

@REM 执行python主代码
python main.py

pause