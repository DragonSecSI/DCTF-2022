$(() => {
  const executeQuery = (text, signature, queryNo) => {
    // text here is base64 encoded
    // signature confirms, that there is nothing malicious in the text
    // queryNo is used to identify the query that will be executed
    $.ajax({
      url: "/execute",
      method: "POST",
      data: {
        // Backend devs said that the text should be base64 encoded
        text,
        signature,
        queryNo,
        //debug:true,
      },
    }).done((data) => {
      if (data.status === "ok") {
        //Write query to pre in html
        $("#query_results").html(`<pre>Executed: ${data.query}</pre>`);
        const results = data.results || [];
        if (data.description) {
          $("#query_results").append(`<p>${data.description}</p>`);
        }
        if (results.length > 0) {
          //Write results into html table
          const fields = Object.keys(results[0]);
          //capitalize first letter of each word
          $("#query_results")
            .append(`<table class="table table-striped table-bordered">
        <thead>
          <tr>
            <th>#</th>
            ${fields
              .map(
                (field) =>
                  `<th>${field.charAt(0).toUpperCase() + field.slice(1)}</th>`
              )
              .join("")}
          </tr>
        </thead>
        <tbody>
          ${results
            .map(
              (result, index) => `<tr>
            <td>${index + 1}</td>
            ${fields.map((field) => `<td>${result[field]}</td>`).join("")}
          </tr>`
            )
            .join("")}
        </tbody>
      </table>`);
        } else {
          $("#query_results").append(`<p>No results found</p>`);
        }
      }
    });
  };

  $("#query_execute").on("click", () => {
    const contents = $("#query_text").val();
    const queryNo = $("#query_no").val();
    if (!contents) {
      alert("Please enter some text");
      return;
    }

    // Because people continously try to break the app,
    // we need to make sure that the text is checked and signed
    $.ajax({
      type: "POST",
      url: "/verify_and_sign_text",
      data: {
        // Backend devs said that the query should be base64 encoded
        text: btoa(contents),
        alg: "sha1",
        //debug:true
      },
    })
      .done((data) => {
        if (data.status === "ok") {
          // Overwrite sanitized query
          $("#query_text").val(atob(data.trimmedText));
          executeQuery(data.trimmedText, data.signature, queryNo);
        } else {
          alert("Error: " + data.message);
        }
      })
      .catch((errdata) => {
        console.error(errdata);
      });
  });
});
