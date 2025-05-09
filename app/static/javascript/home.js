function loadAssignments() {
    $.ajax({
        url: "/api/assignments",
        method: "GET",
        dataType: "json",
        success: function(data) {
            let container = $("#assignments-container");
            container.empty();

            data.forEach(bus => {
                let html = `
                    <div>
                        <h3>${bus.bus_name} - ${bus.spot_name}</h3>
                        <iframe src="/static/maps/map_${bus.bus_name}_${bus.spot_name}.html" width="600" height="400"></iframe>
                        <a href="/static/maps/map_${bus.bus_name}_${bus.spot_name}.html" target="_blank">View Full Map</a>
                    </div>
                `;
                container.append(html);
            });
        },
        error: function() {
            console.error("failed");
        }
    });
}

$(document).ready(loadAssignments);

setInterval(loadAssignments, 10000);