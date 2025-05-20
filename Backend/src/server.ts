import express, { Request, Response } from 'express';
import multer, { StorageEngine } from 'multer';
import cors from 'cors';


const storage: StorageEngine = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  },
});

const app = express();
const upload = multer({ storage: storage });

app.use(cors());

interface MulterRequest extends Request {
  file?: Express.Multer.File;
}

app.post('/upload', upload.single('file'), (req: MulterRequest, res: Response):any => {
  if (!req.file) {
    return res.status(400).send('No file uploaded');
  }

  console.log('Received file:', req.file.originalname);
  res.status(200).send('File uploaded successfully');
});

const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
