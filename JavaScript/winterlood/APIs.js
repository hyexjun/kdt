async function getData() {
  let rawResponse = fetch('https://jsonplaceholder.typicode.com/posts').then((res) => console.log(res));
  let jsonResponse = await rawResponse.json();
  console.log(jsonResponse); // ?? .json() 이거 뭐임??
}

getData();
