import Link from 'next/link';

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 className="text-4xl font-bold text-blue-600">Post-Quantum Encryption</h1>
      <p className="text-gray-600 mt-2">Secure your files with next-generation encryption.</p>
      <div className="mt-6">
        <Link href="/dashboard">
          <a className="px-6 py-2 bg-blue-600 text-white rounded-md">Go to Dashboard</a>
        </Link>
      </div>
    </div>
  );
}
