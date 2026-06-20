# Set error action preference to stop on errors
$ErrorActionPreference = "Stop"

Write-Host "--- Starting Setup for You'll Never Catch Me ---" -ForegroundColor Cyan

# 1. Run your existing Python build process
Write-Host "Executing build.py..." -ForegroundColor Yellow
python build.py

# 2. Check the exit code of the Python process
if ($LASTEXITCODE -eq 0) {
    Write-Host "Build process finished successfully!" -ForegroundColor Green
} else {
    Write-Host "Build failed with exit code $LASTEXITCODE." -ForegroundColor Red
}

Write-Host "--- Setup Complete! ---" -ForegroundColor Cyan