function loadAssignments() {
    $.ajax({
        url: "/home/api/assignments",
        method: "GET",
        dataType: "json",
        success: function (data) {
            let container = $("#assignments-container");
            container.empty();

            data.forEach(bus => {
                let html = `
                    <a class="mt-16 text-success text-decoration-none" href="/static/maps/map_${bus.bus_name}_${bus.spot_name}.html" target="_blank">
                        <div class="container rounded-lg">
                            <div class="card shadow-lg p-3 mb-4 bg-white rounded clickable-card hover-bg">
                                <div class="card-body d-flex align-items-start gap-3">
                                    <iframe class="rounded" src="/static/maps/map_${bus.bus_name}_${bus.spot_name}.html" width="600" height="400"></iframe>
                                    <div>
                                        <h1 class="card-title text-primary display-1 text-success">${bus.bus_name}</h1>
                                        <h1 class="card-title text-primary display-1 text-success">${bus.spot_name}</h1>
                                        <a class="mt-16 text-success" href="/static/maps/map_${bus.bus_name}_${bus.spot_name}.html" target="_blank"> Map Link </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </a>
                `;
                container.append(html);
            });
        },
        error: function () {
            console.error("failed");
        }
    });
}

$(document).ready(loadAssignments);

setInterval(loadAssignments, 10000);