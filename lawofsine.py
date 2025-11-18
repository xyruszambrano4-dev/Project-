<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Law of Sines Triangle</title>
<style>
  body {
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: #f2f2f2;
  }
  canvas {
    border: 1px solid black;
    background: white;
    margin-top: 10px;
  }
  input, button {
    margin: 5px;
    padding: 5px;
  }
</style>
</head>
<body>
<h2>🔺 Law of Sines Triangle Visualizer</h2>

<label>Angle A (°): <input type="number" id="angleA" value="40"></label><br>
<label>Angle B (°): <input type="number" id="angleB" value="70"></label><br>
<label>Side a: <input type="number" id="sideA" value="150"></label><br>
<button onclick="drawTriangle()">Draw Triangle</button>

<canvas id="canvas" width="500" height="400"></canvas>

<p id="output"></p>

<script>
function drawTriangle() {
  const A = parseFloat(document.getElementById("angleA").value);
  const B = parseFloat(document.getElementById("angleB").value);
  const a = parseFloat(document.getElementById("sideA").value);

  const C = 180 - (A + B);

  const A_rad = A * Math.PI / 180;
  const B_rad = B * Math.PI / 180;
  const C_rad = C * Math.PI / 180;

  const b = (a * Math.sin(B_rad)) / Math.sin(A_rad);
  const c = (a * Math.sin(C_rad)) / Math.sin(A_rad);

  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  const startX = 100;
  const startY = 300;

  ctx.beginPath();
  ctx.moveTo(startX, startY);
  ctx.lineTo(startX + a, startY);

  const x2 = startX + a - b * Math.cos(B_rad);
  const y2 = startY - b * Math.sin(B_rad);

  ctx.lineTo(x2, y2);
  ctx.closePath();
  ctx.strokeStyle = "#000";
  ctx.lineWidth = 2;
  ctx.stroke();

  ctx.font = "14px Arial";
  ctx.fillText("A", startX - 20, startY + 15);
  ctx.fillText("B", startX + a + 10, startY + 15);
  ctx.fillText("C", x2 - 10, y2 - 10);

  ctx.fillText("a", startX + a / 2 - 5, startY + 20);
  ctx.fillText("b", (x2 + startX + a) / 2, (y2 + startY) / 2);
  ctx.fillText("c", (x2 + startX) / 2 - 15, (y2 + startY) / 2);

  document.getElementById("output").innerHTML = `
    <b>Results:</b><br>
    Angle A = ${A.toFixed(2)}°, Angle B = ${B.toFixed(2)}°, Angle C = ${C.toFixed(2)}°<br>
    Side a = ${a.toFixed(2)}, Side b = ${b.toFixed(2)}, Side c = ${c.toFixed(2)}
  `;
}
</script>
</body>
</html>
