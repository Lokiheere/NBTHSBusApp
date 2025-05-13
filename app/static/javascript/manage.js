function loadAssignments() {
    $.ajax({
        url: "/management/api/assignments",
        method: "GET",
        dataType: "json",
        success: function (data) {
            let container = $("#undo-assignments-container");
            container.empty();

            data.forEach(bus => {
                let html = `
                    <div class="assignment-entry" data-bus="${bus.bus_name}" data-spot="${bus.spot_name}">
                        <p>Bus: ${bus.bus_name} | Spot: ${bus.spot_name}</p>
                        <button id="undo-btn" data-bus="${bus.bus_name}" data-spot="${bus.spot_name}">Undo Assignment</button>
                    </div>
                `;
                container.append(html);
            });

            $("#undo-btn").on("click", function() {
                let busName = $(this).data("bus_name");
                let spotName = $(this).data("spot_name");
                let entry = $(this).closest(".assignment-entry");

                $.ajax({
                    url: "/management/api/undo_assignments",
                    method: "POST",
                    contentType: "application/json",
                    data: JSON.stringify({ bus_name: busName, spot_name: spotName}),
                    success: function() {
                        entry.remove();
                    },
                    error: function () {
                        console.error("failed");
                    }
                });
            });
        },
        error: function () {
            console.error("failed");
        }
    });
}

$(document).ready(loadAssignments);

setInterval(loadAssignments, 10000);