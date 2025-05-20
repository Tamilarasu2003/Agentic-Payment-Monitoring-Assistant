import React, { useState } from 'react';

const FileUpload = () => {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState('');

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage('Please select a file');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      setUploading(true);
      setMessage('');
      const response = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        setMessage('Upload successful!');
      } else {
        setMessage('Upload failed');
      }
    } catch (error) {
      setMessage('Error uploading file');
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="p-4">
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={uploading} className="ml-2">
        {uploading ? 'Uploading...' : 'Upload'}
      </button>
      {message && <p className="mt-2">{message}</p>}
    </div>
  );
};

export default FileUpload;
