document.getElementById('dataForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const data = document.getElementById('inputData').value;
  const response = await fetch('/data', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ message: data })
  });
  const result = await response.json();
  document.getElementById('response').textContent = JSON.stringify(result);
});
