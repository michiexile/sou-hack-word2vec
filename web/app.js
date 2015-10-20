draw = function(url) {

    width  = $(window).width(); 
    height  = $(window).height(); 
    var color = d3.scale.category20();

    var force = d3.layout.force()
        .charge(-120)
        .linkDistance(130)
        .size([width, height]);
    
    $("svg").remove();
    var svg = d3.select("body").append("svg")
        .attr("width", width)
        .attr("height", height);
    d3.json(url, function(error, graph) {
        //d3.json("exampledata.json", function(error, graph) {
        if (error) throw error;
        force
            .nodes(graph.nodes)
            .links(graph.links)
            .start();

        var link = svg.selectAll(".link")
            .data(graph.links)
            .enter().append("line")
            .attr("class", "link")
            .style("stroke-width", function(d) { return Math.sqrt(d.value); });

        var node = svg.selectAll(".node")
            .data(graph.nodes)
            .enter().append("text")
            .text(function(d) { return d.name; })

            .call(force.drag);

        node.append("title")
            .text(function(d) { return d.name; });

        force.on("tick", function() {
            link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node.attr("x", function(d) { return d.x; })
            .attr("y", function(d) { return d.y; });
        });
    });

    };


back = function(){
    decade -= 10;
    if(decade < 20){ decade = 20; }
    url = decade + "_data.json";
    console.log(url);
    draw(url);
}

forward = function(){

    decade += 10;
    if(decade > 90){ decade = 90; }
    url = decade + "_data.json";
    console.log(url);
    draw(url);
}

decade = 20;

$(document).ready(function(){

    var url = "20_data.json";
    draw(url);

    $('#back').click(back);
    $('#forward').click(forward);
}); 
