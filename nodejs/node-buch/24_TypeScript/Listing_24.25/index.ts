import * as express from 'express';

const app = express();

app.get(
  '/',
  (req: express.Request, res: express.Response): void => {
    res.send('Hello Client');
  },
);

app.listen(8080, () => console.log('Server is listening'));
