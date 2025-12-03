from IPython.display import HTML, display

# This HTML/JS code creates a paste area in the browser
html_code = """
<div style="font-family: sans-serif; padding: 20px; border: 2px dashed #ccc; border-radius: 10px; background-color: #f9f9f9; color: #333; text-align: center;">
    <h3>Image to HTML Base64 Converter</h3>
    <p>Click inside this box and press <b>Ctrl+V</b> (Cmd+V) to paste your screenshot.</p>
    
    <div id="preview" style="margin: 10px 0; max-width: 100%; height: auto; display: none;">
        <p>Preview:</p>
        <img id="img_preview" style="max-width: 200px; border: 1px solid #ddd;">
    </div>

    <textarea id="output_code" rows="5" style="width: 100%; margin-top: 10px; display: none; font-family: monospace; color: #333;" readonly></textarea>
    
    <br>
    <button id="copy_btn" onclick="copyToClipboard()" style="display: none; margin-top: 10px; padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">
        Copy HTML Code
    </button>
    <p id="status" style="color: gray; font-size: 0.9em; margin-top: 10px;">Waiting for paste...</p>
</div>

<script>
// Listen for paste events on the document
document.addEventListener('paste', function(event) {
    var items = (event.clipboardData || event.originalEvent.clipboardData).items;
    
    // Loop through clipboard items to find an image
    for (var index in items) {
        var item = items[index];
        if (item.kind === 'file' && item.type.includes('image/')) {
            var blob = item.getAsFile();
            var reader = new FileReader();
            
            reader.onload = function(event) {
                var base64Data = event.target.result;
                
                // 1. Format the requested HTML string
                var htmlTag = '<img src="' + base64Data + '" style="max-width: 100%; height: auto; border: 1px solid #ccc;">';
                
                // 2. Display in Text Area
                var outputBox = document.getElementById('output_code');
                outputBox.style.display = 'block';
                outputBox.value = htmlTag;
                
                // 3. Show Preview
                var imgPreview = document.getElementById('img_preview');
                document.getElementById('preview').style.display = 'block';
                imgPreview.src = base64Data;
                
                // 4. Show Copy Button
                document.getElementById('copy_btn').style.display = 'inline-block';
                document.getElementById('status').innerText = "Image converted! Click Copy below.";
                document.getElementById('status').style.color = "green";
            };
            
            reader.readAsDataURL(blob);
        }
    }
});

function copyToClipboard() {
    var copyText = document.getElementById("output_code");
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices
    navigator.clipboard.writeText(copyText.value).then(function() {
        var btn = document.getElementById('copy_btn');
        btn.innerText = "Copied!";
        btn.style.backgroundColor = "#008CBA";
        setTimeout(() => {
            btn.innerText = "Copy HTML Code";
            btn.style.backgroundColor = "#4CAF50";
        }, 2000);
    });
}
</script>
"""

display(HTML(html_code))