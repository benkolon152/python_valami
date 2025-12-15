export default async function handler(req, res) {
    const {method, body} = req;
    console.log('body', body)

    return res.sendStatus(201)
}