var scale_factor = 1.0; //zoom 
var render_style = "ellipse"; //default 
var neos=[];
var mbas=[];
const AU = 149.6;

function get_center_point(canvas)
{
    //retina screen detection
    if (window.devicePixelRatio > 1) return [canvas.width/4, canvas.height/4]
    else return [canvas.width/2, canvas.height/2]
}
function drawCenter(canvas) {

    const ctx = canvas.getContext("2d");
    var center_point = get_center_point(canvas);
    ctx.beginPath();
    ctx.arc(center_point[0], center_point[1], 8, 0, 2*Math.PI);
    ctx.fillStyle = 'yellow';
    ctx.fill();
    ctx.stroke();
}

function draw_xy_axis(canvas)
{
    var center_point= get_center_point(canvas);
    var center_x = center_point[0];
    var center_y = center_point[1];
    const ctx = canvas.getContext("2d");
    ctx.strokeStyle = "white";
    ctx.beginPath();
    ctx.moveTo(center_x, 50);
    ctx.lineTo(center_x, 600);
    //draw notches
    for (var t=-250*scale_factor; t<=250*scale_factor; t=t+50*scale_factor)
    {
        ctx.moveTo(center_x-10, center_y+t/scale_factor);
        ctx.lineTo(center_x+10, center_y+t/scale_factor);
    }
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(50, center_y);
    ctx.lineTo(1200, center_y);
    //draw notches
    for (var t=-550*scale_factor; t<=550*scale_factor; t=t+50*scale_factor)
    {
        ctx.moveTo(center_x+t/scale_factor, center_y-10);
        ctx.lineTo(center_x+t/scale_factor, center_y+10);
    }
    ctx.stroke();
}

function draw_asteroid(canvas, asteroid, color)
{
    var au=AU/scale_factor;
    var eccentricity = asteroid.eccentricity
    var semiMajorAxis = asteroid.semimajor_a*au;
    var argPeriapsis = asteroid.argument_perihelion;
    var angle = asteroid.argument_perihelion*(Math.PI/180);
    drawOrbitEllipse(canvas, semiMajorAxis, argPeriapsis, eccentricity, color, true);

}

function drawOrbitEllipse(canvas, semiMajorAxis, argPeriapsis, eccentricity, p_color, is_asteroid=false)
{
    const selectElement = document.getElementById('view_type');
    const view_type = selectElement.value;
    const ctx = canvas.getContext("2d");
    var center_point= get_center_point(canvas);
    var sunX = center_point[0];
    var sunY = center_point[1];

    const focalDistance = semiMajorAxis * eccentricity;
    const semiMinorAxis = semiMajorAxis * Math.sqrt(1 - eccentricity * eccentricity);
  
    // Calculate center of the ellipse
    const centerX = sunX + focalDistance * Math.cos(argPeriapsis);
    const centerY = sunY + focalDistance * Math.sin(argPeriapsis);
  
    if (is_asteroid) ctx.lineWidth=1;
    else ctx.lineWidth=3; 

    // Draw the elliptical orbit
    ctx.beginPath();

    if (is_asteroid)
    {
        if (view_type=="1")
            ctx.ellipse(centerX, centerY, semiMajorAxis, semiMinorAxis, argPeriapsis, 0,2*Math.PI);
        if (view_type=="2") 
        {
            var start = Math.random()*2*Math.PI;
            var stop = start+0.001;
            ctx.ellipse(centerX, centerY, semiMajorAxis, semiMinorAxis, argPeriapsis, start, stop);//0, 2 * Math.PI);
        }
    }
    else
        ctx.ellipse(centerX, centerY, semiMajorAxis, semiMinorAxis, argPeriapsis, 0, 2 * Math.PI);

    ctx.strokeStyle = p_color;
    ctx.stroke();
}

function draw_all_asteroids()
{
    const canvas = document.getElementById("canvasMap");
    for (a in neos) draw_asteroid(canvas, neos[a], "yellow");
    for (b in mbas) draw_asteroid(canvas, mbas[b], "white");

}
function render_page(reload)
{
    const canvas = document.getElementById("canvasMap");
    const ctx = canvas.getContext("2d");
    ctx.canvas.width  = window.innerWidth;
    ctx.canvas.height = window.innerHeight;

    const selectElement = document.getElementById('asteroid_type');
    const asteroid_type = selectElement.value;
    if (asteroid_type == 'one')
    {
        var mpc_id = document.getElementById("mpc_id_name").value;
        console.log(mpc_id);
    }
    //setup page - retina screen only!
    if (window.devicePixelRatio > 1) {
        var canvasWidth = canvas.width;
        var canvasHeight = canvas.height;

        canvas.width = canvasWidth * window.devicePixelRatio;
        canvas.height = canvasHeight * window.devicePixelRatio;
        canvas.style.width = canvasWidth + "px";
        canvas.style.height = canvasHeight + "px";
        ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
    }
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawCenter(canvas);
    draw_xy_axis(canvas);

    //load asteroids if required
    if (reload==1)
    {
        const xhttp = new XMLHttpRequest();
        xhttp.onload = function() {
            // What to do when the response is ready
            data = JSON.parse(this.responseText);
            neos = data["pha"]
            mbas = data["mba"]
            draw_all_asteroids();
        }
        if (asteroid_type == 'one')
        {
            xhttp.open("GET", "get_data?subset="+asteroid_type+"&mpc_id="+mpc_id, true);
        }
        else
            xhttp.open("GET", "get_data?subset="+asteroid_type, true);
        xhttp.send();
    }
    else
    {
        draw_all_asteroids();
    }
    //Outer planets
    document.getElementById("canvasMap").focus();            
    drawOrbitEllipse(canvas, 4500.0/scale_factor, 273.867, 0.0489, "blue", false); 
    drawOrbitEllipse(canvas, 2870.972/scale_factor, 96.998, 0.04717, "white", false); 
    drawOrbitEllipse(canvas, 1433.53/scale_factor, 339.392, 0.0565, "green", false); 
    drawOrbitEllipse(canvas, 778.479/scale_factor, 273.867, 0.0489, "brown", false); 
    //Draw inner planets
    drawOrbitEllipse(canvas, 227.93/scale_factor, 286.50, 0.0934, "red", false);           
    drawOrbitEllipse(canvas, 149.6/scale_factor, 114.20783, 0.0167086, "green", false);
    drawOrbitEllipse(canvas, 108.21/scale_factor, 54.884, 0.006772, "blue", false);
    drawOrbitEllipse(canvas, 57.91/scale_factor, 29.124, 0.20563, "orange", false);
    //draw scale
    ctx.font = "24px serif";
    ctx.fillStyle = "white";
    ctx.fillText("Scale: "+Math.round(550/AU*scale_factor) + " au", 10, 600);
}
function init() {
    document.addEventListener('keydown', function(event) {
    switch(event.key) {
        case '+':
            console.log('Plus key pressed');
            scale_factor = scale_factor/2;
            render_page(0);
            break;
        case '-':
            console.log('Minus key pressed');
            scale_factor = scale_factor*2;
            render_page(0);
            break;
        }
    });
    const text_input = document.getElementById("mpc_id_name");
    text_input.addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        render_page(1);
    }
});
    render_page(1);
}