const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

console.log('====================================================');
console.log('  Starting PashuCare AI Full-Stack Application...  ');
console.log('====================================================');

// Find Python path
let pythonPath = 'python';
const venvWin = path.join(__dirname, 'backend', 'venv', 'Scripts', 'python.exe');
const venvUnix = path.join(__dirname, 'backend', 'venv', 'bin', 'python');

if (fs.existsSync(venvWin)) {
  pythonPath = `"${venvWin}"`;
} else if (fs.existsSync(venvUnix)) {
  pythonPath = `"${venvUnix}"`;
}

// 1. Start FastAPI Backend
console.log('[Backend] Starting FastAPI server on http://127.0.0.1:8000 ...');
const backend = spawn(
  pythonPath,
  ['-m', 'uvicorn', 'app.main:app', '--host', '127.0.0.1', '--port', '8000', '--reload'],
  { cwd: path.join(__dirname, 'backend'), shell: true, stdio: 'inherit' }
);

// 2. Start Vite Frontend
console.log('[Frontend] Starting React (Vite) development server...');
const frontend = spawn(
  'npm',
  ['run', 'dev'],
  { cwd: path.join(__dirname, 'frontend'), shell: true, stdio: 'inherit' }
);

// Cleanup on exit
const cleanup = () => {
  console.log('\nStopping servers...');
  backend.kill();
  frontend.kill();
  process.exit();
};

process.on('SIGINT', cleanup);
process.on('SIGTERM', cleanup);
process.on('exit', cleanup);
