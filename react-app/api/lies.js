export default async function handler(req, res) {
    const method = req.method
    if (method == 'POST'){
        const body = req.body
        console.log('body', body)
        return res.sendStatus(201)
    } else {
        return res.sendStatus(405)
    }
}