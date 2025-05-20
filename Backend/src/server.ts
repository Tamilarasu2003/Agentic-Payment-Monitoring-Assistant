import express, { Request, Response } from 'express';
import multer from 'multer';
import cors from 'cors';
import path from 'path';
import fs from 'fs';

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(cors());

// Define file type for request with file
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
