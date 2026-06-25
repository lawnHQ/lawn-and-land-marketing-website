export default async function handler(req, res) {
  if (req.method === 'OPTIONS') {
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    return res.status(204).end();
  }

  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST, OPTIONS');
    return res.status(405).json({ ok: false, error: 'method_not_allowed' });
  }

  try {
    const report = typeof req.body === 'string' ? safeParse(req.body) : req.body;
    const payload = report && (report['csp-report'] || report);
    const summary = {
      blocked_uri: payload?.['blocked-uri'] || payload?.blockedURL || null,
      violated_directive: payload?.['violated-directive'] || payload?.effectiveDirective || null,
      document_uri: payload?.['document-uri'] || payload?.documentURL || null,
      source_file: payload?.['source-file'] || payload?.sourceFile || null,
      line_number: payload?.['line-number'] || payload?.lineNumber || null,
      disposition: payload?.disposition || 'report'
    };
    console.warn('csp_report', JSON.stringify(summary));
  } catch (err) {
    console.warn('csp_report_parse_error', err && err.message ? err.message : String(err));
  }

  return res.status(204).end();
}

function safeParse(value) {
  try { return JSON.parse(value); }
  catch { return { raw: String(value).slice(0, 1000) }; }
}
