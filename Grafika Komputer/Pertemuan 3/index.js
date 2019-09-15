(function() {
    var canvas;
    var gl;
    var program;

    glUtils.SL.init({
         callback:function() { 
            main(); 
        } 
    });

    function main() {
        //Menambahkan event untuk resizer
        window.addEventListener('resize', resizer);

        var VSHADER_SOURCE = glUtils.SL.Shaders.v1.vertex;
        var FSHADER_SOURCE = glUtils.SL.Shaders.v1.fragment;
    
        canvas = document.getElementById('glcanvas');
        gl = glUtils.checkWebGL(canvas);

        initGlSize();

        // Inisialisasi shaders dan program
        var vertexShader = glUtils.getShader(gl, gl.VERTEX_SHADER, VSHADER_SOURCE);
        var fragmentShader = glUtils.getShader(gl, gl.FRAGMENT_SHADER, FSHADER_SOURCE);

        program = glUtils.createProgram(gl, vertexShader, fragmentShader);
    
        gl.useProgram(program);
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

    function initBuffers(coord, N) {
        var vertices = coord;

        // Jumlah vertices
        var n = N;

        var vertexBuffer = gl.createBuffer();
        if(!vertexBuffer) {
            console.log('gagal membuat objek buffer');
            return -1;
        }

        // bind buffer object to target
        // target: ARRAY_BUFFER, ELEMENT_ARRAY_BUFFER
        gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
        //write data ke buffer object
        //STATIC_DRAW, STREAM_DRAW, DYNAMIC_DRAW
        gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

        //get attribute aposition
        var aPosition = gl.getAttribLocation(program, 'aPosition');
        if(aPosition < 0) {
            console.log('Failed get location of aposition');
            return -1;
        }
        // https://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttribPointer.xml
        gl.vertexAttribPointer(aPosition, 2, gl.FLOAT, false, 0, 0);

        //Enable assignment to aPosition variable
        gl.enableVertexAttribArray(aPosition);

        return n;
    }

    function draw() {
        var leftVertices = new Float32Array([
            -0.6, 0.4,
            -0.6, -0.4,
            -0.5, -0.4,
            -0.5, -0.02,
            -0.15, -0.02,
            -0.15, 0.1,
            -0.5, 0.1,
            -0.5, 0.28,
            -0.23, 0.28,
            -0.15, 0.4
        ]);

        var rightVertices1 = new Float32Array([
            0.1, 0.4,
            0.1, -0.4,
            0.2, -0.4,
            0.2, 0.4,
            0.1, 0.4
        ]);

        var rightVertices2 = new Float32Array([
            0.1, 0.4,
            0.5, 0.4,
            0.42, 0.28,
            0.1, 0.28,
            0.1, 0.4
        ]);

        var rightVertices3 = new Float32Array([
            0.1, 0.1,
            0.5, 0.1,
            0.1, -0.02,
            0.5, -0.02
        ]);
        
        // Bersihkan layar menjadi hitam
        gl.clearColor(0.0, 0.0, 0.0, 1.0);

        // Bersihkan buffernya canvas
        gl.clear(gl.COLOR_BUFFER_BIT);

        // custom: POINTS, LINES, LINE_STRIP, LINE_LOOP
        // TRIANGLES, TRIANGLE_STRIP
        var gambarKiri = initBuffers(leftVertices, 10);
        gl.drawArrays(gl.LINE_LOOP, 0, gambarKiri);
        
        var gambarKanan1 = initBuffers(rightVertices1, 5);  
        gl.drawArrays(gl.TRIANGLE_STRIP, 0, gambarKanan1);

        var gambarKanan2 = initBuffers(rightVertices2, 5);
        gl.drawArrays(gl.TRIANGLE_STRIP, 0, gambarKanan2);

        var gambarKanan3 = initBuffers(rightVertices3, 4);
        gl.drawArrays(gl.TRIANGLE_STRIP, 0, gambarKanan3);
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