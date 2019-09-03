(function(global) {
    var glUtils = {
        VERSION: '0.0.1',
        checkWebGL: function(canvas) {
            var contexts = ['webgl', 'experimental-webgl', 'webkit-3d', 'moz-webgl'];
            var gl;
            for (var i = 0; i < contexts.length; i++) {
                try {
                    var context = contexts[i];
                    gl = canvas.getContext(context);
                } catch (error) {
        
                }
                if(gl) {
                    break;
                }        
            }
            if(!gl) {
                alert("web gl tidak ditemukan, tolong gunakan versi terbaru chrome atau firefox");
            }
            return gl;
        },
        getShader: function(gl, type, source) {
            var shader = gl.createShader(type);
            gl.shaderSource(shader, source);
            gl.compileShader(shader);
            if(!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
                console.log('Shader gagal dikompilasi: ' + gl.getShaderInfoLog(shader));
                gl.deleteShader(shader);
                return null;
            }

            return shader;
        },
        createProgram: function(gl, vertexShader, fragmentShader) {
            var program = gl.createProgram();
            gl.attachShader(program, vertexShader);
            gl.attachShader(program, fragmentShader);
            gl.linkProgram(program);

            // Cek apakah link-nya berhasil
            if(!gl.getProgramParameter(program, gl.LINK_STATUS)) {
                var error = gl.getProgramInfoLog(program);
                console.log('Gagal link: ' + error);
                gl.deleteProgram(program);
                gl.deleteShader(vertexShader);
                gl.deleteShader(fragmentShader);
                return null;
            }
            
            gl.validateProgram(program);
            if(!gl.getProgramParameter(program, gl.VALIDATE_STATUS)) {
                var error = gl.getProgramInfoLog(program);
                console.log('Gagal validasi: ' + error);
                gl.deleteProgram(program);
                gl.deleteShader(vertexShader);
                gl.deleteShader(fragmentShader);
                return null;
            }
            return program;
        },
        SL: {
            sourceFromHtml: function(options) {
                var options = options || {};
                this.elemName = options.elemName || 'shader';
                this.dataType = options.dataType || 'data-type';
                this.dataVersion = options.dataVersion || 'data-version';
                this.shaderElems = document.getElementsByName(this.elemName);
                this.Shaders = this.Shaders || {};
                this.slShaderCount = this.shaderElems.length;
                for (let i = 0; i < this.slShaderCount; i++) {
                    var shader = this.shaderElems[i];
                    if(!shader) {
                        return null;
                    }

                    var source = "";
                    var currentChild = shader.firstChild;
                    while(currentChild) {
                        if(currentChild.nodeType == currentChild.TEXT_NODE) {
                            source += currentChild.textContent;
                        }
                        currentChild = currentChild.nextSibling;
                    }

                    var version = shader.getAttribute(this.dataVersion);
                    if(!this.Shaders[version]) {
                        this.Shaders[version] = {
                            vertex: '',
                            fragment: ''
                        };
                    }
                    this.Shaders[version][shader.getAttribute(this.dataType)] = source;
                }
            }
        }
    };

    global.glUtils = glUtils;
})(window || this);