@echo off

for /f "tokens=2" %%a in ('type go.mod ^| findstr /r "^module"') do set PKGAGE=%%a

:generate
protoc --proto_path=. --go_opt=module=%PKGAGE% --go_out=. proto\*.proto

echo Completed build process.
