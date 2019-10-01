precision mediump float;

attribute vec2 vPosition;
attribute vec3 vColor;
varying vec3 fColor;
uniform float theta;
uniform float scale;

void main() {
  fColor = vColor;
  mat4 translasi = mat4(
    1.0, 0.0, 0.0, 1.4,
    0.0, 1.0, 0.0, 0.0,
    0.0, 0.0, 1.0, 0.0,
    0.0, 0.0, 0.0, 1.0
  );

  mat4 rotasiX = mat4(
    cos(theta), -sin(theta), 0.0, 0.45*cos(theta)-0.45,
    sin(theta), cos(theta), 0.0, 0.45 * sin(theta),
    0.0, 0.0, 1.0, 0.0,
    0.0, 0.0, 0.0, 1.0
  );

  mat4 skalasi = mat4(
    1.0, 0.0, 0.0, 0.0,
    0.0, 1.0, 0.0, 0.0,
    0.0, 0.0, 1.0, 0.0,
    0.0, 0.0, 0.0, 1.0
  );

  gl_Position = vec4(vPosition, 0.0, 1.0) * skalasi;
  gl_Position *= rotasiX;
}
