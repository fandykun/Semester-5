(function() {
    var canvas;
    var gl;
    var program;
    var program2;
    let theta = 0;
    let scale = 0;
    var inc = 0.0118;
    
    glUtils.SL.init({
         callback:function() { 
            main(); 
        } 
    });

    function main() {
        //Menambahkan event untuk resizer
        window.addEventListener('resize', resizer);

        canvas = document.getElementById('glcanvas');
        gl = glUtils.checkWebGL(canvas);

        initGlSize();

        // Inisialisasi shaders dan program
        var vertexShader = glUtils.getShader(gl, gl.VERTEX_SHADER, glUtils.SL.Shaders.v1.vertex);
        var vertexShader2 = glUtils.getShader(gl, gl.VERTEX_SHADER, glUtils.SL.Shaders.v2.vertex);

        var fragmentShader = glUtils.getShader(gl, gl.FRAGMENT_SHADER, glUtils.SL.Shaders.v1.fragment);

        program = glUtils.createProgram(gl, vertexShader, fragmentShader);
        program2 = glUtils.createProgram(gl, vertexShader2, fragmentShader);
        resizer();
    }

    function initGlSize() {
        var width = canvas.getAttribute('width');
        var height = canvas.getAttribute('height');
        if(width) {
            gl.maxWidth = width;
        }
        if(height) {
            gl.maxHeight = height;
        }
    }

    function initBuffers(coord, N, glProgram) {
        var vertices = coord;

        // Jumlah vertices
        var n = N;

        var vertexBuffer = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

        //get attribute aposition
        var vPosition = gl.getAttribLocation(glProgram, 'vPosition');
        var vColor = gl.getAttribLocation(glProgram, 'vColor');
        
        gl.vertexAttribPointer(vPosition, 2, gl.FLOAT, gl.FALSE, 5 * Float32Array.BYTES_PER_ELEMENT, 0);
        gl.vertexAttribPointer(vColor, 3, gl.FLOAT, gl.FALSE, 5 * Float32Array.BYTES_PER_ELEMENT, 2 * Float32Array.BYTES_PER_ELEMENT);

        //Enable assignment to aPosition variable
        gl.enableVertexAttribArray(vPosition);
        gl.enableVertexAttribArray(vColor);

        gl.useProgram(glProgram);

        var thetaLoc = gl.getUniformLocation(glProgram, 'theta');
        var scaleLoc = gl.getUniformLocation(glProgram, 'scale');
        gl.uniform1f(thetaLoc, theta);
        gl.uniform1f(scaleLoc, scale);
        return n;
    }

    function draw() {

        function render() {
            var leftVertices = new Float32Array([
                -0.6, 0.4, 1.0, 0.8, 0.0,
                -0.6, -0.4, 0.9, 0.8, 0.1,
                -0.5, -0.4, 0.8, 0.8, 0.2,
                -0.5, -0.02, 0.7, 0.8, 0.3,
                -0.15, -0.02, 0.6, 0.8, 0.4,
                -0.15, 0.1, 0.5, 0.8, 0.5,
                -0.5, 0.1, 0.4, 0.8, 0.6,
                -0.5, 0.28, 0.3, 0.8, 0.7,
                -0.23, 0.28, 0.2, 0.8, 0.8,
                -0.15, 0.4, 0.1, 0.8, 0.9
            ]);
            var randomize = Math.random();
            var randomize2 = Math.random();
            var randomize3 = randomize2;
            var rightVertices = new Float32Array([
                0.55, 0.4, randomize2, randomize, randomize3,
                0.47, 0.28, randomize, randomize3, randomize2,
                0.1, 0.4, randomize3, randomize2, randomize,
                0.2, 0.28, randomize2, randomize3, randomize,
                0.1, -0.4, randomize, randomize2, randomize3,
                0.2, -0.4, randomize, randomize3, randomize2,
                0.2, -0.4, randomize3, randomize2, randomize,
                0.2, 0.1, randomize2, randomize3, randomize,
                0.2, 0.1, randomize, randomize2, randomize3,
                0.55, 0.1, randomize, randomize3, randomize2,
                0.2, -0.02, randomize3, randomize2, randomize,
                0.55, -0.02, randomize2, randomize3, randomize,
            ]);

            // Bersihkan layar jadi hitam
            gl.clearColor(0.0, 0.0, 0.0, 1.0);
          
            // Bersihkan buffernya canvas
            gl.clear(gl.COLOR_BUFFER_BIT);
            
            theta += Math.PI * 0.0118;
            
            if(scale > 1){
                inc = -0.0118;
            }
            else if(scale < -1){
                inc = 0.0118;
            }
            scale += inc;

            // custom: POINTS, LINES, LINE_STRIP, LINE_LOOP
            // TRIANGLES, TRIANGLE_STRIP
            var gambarKiri = initBuffers(leftVertices, 10, program2);
            gl.drawArrays(gl.LINE_LOOP, 0, gambarKiri);

            var gambarKanan = initBuffers(rightVertices, 12, program);
            gl.drawArrays(gl.TRIANGLE_STRIP, 0, gambarKanan);

            requestAnimationFrame(render);
        }
        render();
    }

    function resizer() {
        if (!canvas.getAttribute("width") || canvas.getAttribute("width") < 0) {
            canvas.width = window.innerWidth;
            gl.maxWidth = window.innerWidth;
        }
        if (!canvas.getAttribute("height") || canvas.getAttribute("height") < 0) {
            canvas.height = window.innerHeight;
            gl.maxHeight = window.innerHeight;
        }

        //re-scale
        var min = Math.min.apply(Math, [gl.maxWidth, gl.maxHeight, window.innerWidth, window.innerHeight]);
        canvas.width = min;
        canvas.height = min;

        gl.viewport(0, 0, gl.canvas.width, gl.canvas.height);
        draw();
        console.log('resized');
    }
})();