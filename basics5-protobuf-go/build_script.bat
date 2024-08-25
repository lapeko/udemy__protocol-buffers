@echo off

for /f "tokens=2" %%a in ('type go.mod ^| findstr /r "^module"') do set PKGAGE=%%a

:generate
protoc --proto_path=. --go_opt=module=%PKGAGE% --go_out=. proto\*.proto

:build
go build
:clean
del /Q proto\*.pb.go
del /Q proto-go-course.exe

echo Completed build process.
