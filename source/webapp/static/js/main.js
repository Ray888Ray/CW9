
async function makeRequest(url, method='GET') {
    let response = await fetch(url, {method});
    if (response.ok) {
        return await response.json();    }
    else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function AcceptButtonClick(event) {
    let target = event.target;
    console.log(target)
    let url = target.dataset.indexLink;
    console.log(url)
    let id = target.dataset.accept;
    console.log(id)
    let response = await makeRequest(url);
    console.log(response)




}

async function CancelButtonClick(event) {
    let target = event.target;
    let url = target.dataset.indexLink;
    let id = target.dataset.cancel;
    let response = await makeRequest(url);
    console.log(response)
}