(function() {

    glUtils.SL.sourceFromHtml();
    var VSHADER_SOURCE = glUtils.SL.Shaders.v1.vertex;
    var FSHADER_SOURCE = glUtils.SL.Shaders.v1.fragment;

    var canvas = document.getElementById('glcanvas');
    var gl = glUtils.checkWebGL(canvas);

    // Inisialisasi shaders dan program
    var vertexShader = glUtils.getShader(gl, gl.VERTEX_SHADER, VSHADER_SOURCE);
    var fragmentShader = glUtils.getShader(gl, gl.FRAGMENT_SHADER, FSHADER_SOURCE);
    var program = glUtils.createProgram(gl, vertexShader, fragmentShader);

    gl.useProgram(program);

    // Bersihkan layar dari hitam
    gl.clearColor(0.0, 0.0, 0.0, 1.0);

    // Bersihkan buffernya canvas
    gl.clear(gl.COLOR_BUFFER_BIT);

    gl.drawArrays(gl.POINTS, 0, 1);
})();