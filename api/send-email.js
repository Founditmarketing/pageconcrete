import { Resend } from 'resend';

const resend = new Resend(process.env.RESEND_API_KEY);

function esc(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { first_name, last_name, email, phone, address, message } = req.body ?? {};

  if (!email || !message) {
    return res.status(400).json({ error: 'Email and message are required.' });
  }

  const name = [first_name, last_name].filter(Boolean).join(' ') || 'Website Visitor';

  const { error } = await resend.emails.send({
    from: 'Page Concrete <hello@pageconcretenc.com>',
    to: ['nacinc4@gmail.com'],
    replyTo: email,
    subject: `New Quote Request from ${name}`,
    html: `
      <div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto">
        <h2 style="color:#0047ab">New Contact Form Submission</h2>
        <table style="border-collapse:collapse;width:100%">
          <tr><td style="padding:8px;font-weight:bold;width:140px">Name</td><td style="padding:8px">${esc(name)}</td></tr>
          <tr style="background:#f5f5f5"><td style="padding:8px;font-weight:bold">Email</td><td style="padding:8px">${esc(email)}</td></tr>
          <tr><td style="padding:8px;font-weight:bold">Phone</td><td style="padding:8px">${esc(phone) || '—'}</td></tr>
          <tr style="background:#f5f5f5"><td style="padding:8px;font-weight:bold">Project Address</td><td style="padding:8px">${esc(address) || '—'}</td></tr>
        </table>
        <h3 style="color:#0047ab;margin-top:20px">Message</h3>
        <p style="white-space:pre-wrap;background:#f5f5f5;padding:12px;border-radius:4px">${esc(message)}</p>
        <hr style="margin-top:24px;border:none;border-top:1px solid #ddd">
        <p style="color:#999;font-size:12px">Sent from the contact form at pageconcretenc.com</p>
      </div>
    `,
  });

  if (error) {
    console.error('Resend error:', error);
    return res.status(500).json({ error: 'Failed to send message. Please try again.' });
  }

  return res.status(200).json({ ok: true });
}
