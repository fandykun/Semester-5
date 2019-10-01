(function() {

  glUtils.SL.init({ callback: function() { main(); } });

  function main() {
    var canvas = document.getElementById("glcanvas");
    var gl = glUtils.checkWebGL(canvas);
  
    // Inisialisasi shaders dan program
    // console.log("\nVERTEX SOURCE CODE:\n" + glUtils.SL.Shaders.v1.vertex);
    // console.log("\nFRAGMENT SOURCE CODE:\n" + glUtils.SL.Shaders.v1.fragment);
    var vertexShader = glUtils.getShader(gl, gl.VERTEX_SHADER, glUtils.SL.Shaders.v1.vertex);
    var fragmentShader = glUtils.getShader(gl, gl.FRAGMENT_SHADER, glUtils.SL.Shaders.v1.fragment);
    var program = glUtils.createProgram(gl, vertexShader, fragmentShader);
  
    // Definisi verteks dan buffer
    var triangleVertices = [
      // x, y       r, g, b
      0.0, 0.5,     1.0, 0.0, 0.0,
      -0.5, -0.5,   0.0, 0.0, 1.0,
      0.5, -0.5,    0.0, 1.0, 0.0
    ];
    var triangleVertexBufferObject = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, triangleVertexBufferObject);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(triangleVertices), gl.STATIC_DRAW);

    var vPosition = gl.getAttribLocation(program, 'vPosition');
    var vColor = gl.getAttribLocation(program, 'vColor');
    gl.vertexAttribPointer(vPosition, 2, gl.FLOAT, gl.FALSE, 5 * Float32Array.BYTES_PER_ELEMENT, 0);
    gl.vertexAttribPointer(vColor, 3, gl.FLOAT, gl.FALSE, 5 * Float32Array.BYTES_PER_ELEMENT, 2 * Float32Array.BYTES_PER_ELEMENT);

    gl.enableVertexAttribArray(vPosition);
    gl.enableVertexAttribArray(vColor);
  
    gl.useProgram(program);

    var thetaLoc = gl.getUniformLocation(program, 'theta');
    let theta = 0.0;

    var scaleLoc = gl.getUniformLocation(program, 'scale');
    let scale = 1.0;
    
    function render() {
      theta += Math.PI * 0.01;
      gl.uniform1f(thetaLoc, theta);
      gl.uniform1f(scaleLoc, scale);
      // Bersihkan layar jadi hitam
      gl.clearColor(0.0, 0.0, 0.0, 1.0);
    
      // Bersihkan buffernya canvas
      gl.clear(gl.COLOR_BUFFER_BIT);
    
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      requestAnimationFrame(render);
    }
    render();
  }

})();
