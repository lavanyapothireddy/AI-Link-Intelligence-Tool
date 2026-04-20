async function analyzeLink() {

    const url = document.getElementById("urlInput").value;

    if (!url) {
        alert("Please enter URL");
        return;
    }

    document.getElementById("status").innerText = "Analyzing...";

    try {
        const response = await fetch(
            `http://127.0.0.1:8000/analyze?url=${encodeURIComponent(url)}`
        );

        const data = await response.json();

        document.getElementById("url").innerText = data.url;
        document.getElementById("summary").innerText = data.summary;
        document.getElementById("category").innerText = data.category;
        document.getElementById("safety").innerText = data.url_safety;

        document.getElementById("status").innerText = "Done ✅";

    } catch (error) {
        console.log(error);
        document.getElementById("status").innerText = "❌ Backend Error";
    }
}
