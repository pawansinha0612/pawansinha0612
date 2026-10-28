"""Writes assets/banner-dark.svg and assets/banner-light.svg (same layout, two palettes)."""
from pathlib import Path

THEMES = {
    "dark": dict(bg="#0d1117", panel="#161b22", border="#30363d", text="#e6edf3", muted="#8b949e",
                 accent="#58a6ff", ok="#3fb950", warn="#d29922", glow="#1f6feb", chip="#21262d"),
    "light": dict(bg="#ffffff", panel="#f6f8fa", border="#d0d7de", text="#1f2328", muted="#59636e",
                  accent="#0969da", ok="#1a7f37", warn="#9a6700", glow="#54aeff", chip="#eaeef2"),
}

# (label, detail, result) for each line of the test run
STEPS = [
    ("functional &amp; regression", "manual · exploratory", "142 passed"),
    ("api tests", "REST · contract · negative", "86 passed"),
    ("e2e automation", "Playwright · 3 browsers", "54 passed"),
    ("performance", "k6 · 5,000 VUs · p95 412 ms", "SLA met"),
]

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"


def svg(t):
    rows = []
    for i, (label, detail, result) in enumerate(STEPS):
        y = 150 + i * 34
        delay = 0.6 + i * 0.7
        rows.append(f"""
    <g class="step" style="animation-delay:{delay:.1f}s">
      <text x="660" y="{y}" class="mono ok">✓</text>
      <text x="684" y="{y}" class="mono txt">{label}</text>
      <text x="684" y="{y + 15}" class="mono mut small">{detail}</text>
      <text x="1112" y="{y}" class="mono ok" text-anchor="end">{result}</text>
    </g>""")
    done = 0.6 + len(STEPS) * 0.7
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="380" viewBox="0 0 1200 380" role="img" aria-labelledby="title desc">
  <title id="title">Pawan Sinha: QA, Test Automation and Performance Engineering</title>
  <desc id="desc">A terminal running a release gate: functional, API, Playwright and k6 checks pass, release GO.</desc>
  <defs>
    <radialGradient id="glow" cx="0.18" cy="0.2" r="0.7">
      <stop offset="0" stop-color="{t['glow']}" stop-opacity="0.22"/>
      <stop offset="1" stop-color="{t['glow']}" stop-opacity="0"/>
    </radialGradient>
    <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="{t['border']}" stroke-opacity="0.35" stroke-width="1"/>
    </pattern>
  </defs>
  <style>
    .sans {{ font-family: {SANS}; }}
    .mono {{ font-family: {MONO}; font-size: 15px; }}
    .small {{ font-size: 12px; }}
    .txt {{ fill: {t['text']}; }}
    .mut {{ fill: {t['muted']}; }}
    .ok {{ fill: {t['ok']}; font-weight: 600; }}
    .acc {{ fill: {t['accent']}; }}
    .step {{ opacity: 0; animation: in .5s ease-out forwards; }}
    .final {{ opacity: 0; animation: in .5s ease-out {done:.1f}s forwards; }}
    .pulse {{ animation: pulse 2.4s ease-in-out {done + 0.5:.1f}s infinite; transform-origin: 1040px 320px; }}
    .cursor {{ animation: blink 1s step-end infinite; }}
    .bar {{ animation: fill {done - 0.4:.1f}s ease-in-out .4s forwards; transform: scaleX(0); transform-origin: 660px 0; }}
    @keyframes in {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    @keyframes fill {{ to {{ transform: scaleX(1); }} }}
    @keyframes pulse {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: .55; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .step, .final {{ animation: none; opacity: 1; }}
      .bar {{ animation: none; transform: none; }}
      .pulse, .cursor {{ animation: none; }}
    }}
  </style>

  <rect width="1200" height="380" rx="16" fill="{t['bg']}"/>
  <rect width="1200" height="380" rx="16" fill="url(#grid)"/>
  <rect width="1200" height="380" rx="16" fill="url(#glow)"/>

  <!-- left: who -->
  <text x="64" y="104" class="mono acc" font-size="15">$ whoami</text>
  <text x="62" y="160" class="sans txt" font-size="52" font-weight="800" letter-spacing="-1">Pawan Sinha</text>
  <text x="64" y="200" class="sans txt" font-size="22" font-weight="600">QA · Test Automation · Performance Engineering</text>
  <text x="64" y="234" class="sans mut" font-size="16">12+ years keeping banking, payments and lottery systems</text>
  <text x="64" y="256" class="sans mut" font-size="16">fast and reliable when it matters most.</text>

  <g class="sans" font-size="13" font-weight="600">
    <rect x="64" y="290" width="150" height="30" rx="15" fill="{t['chip']}" stroke="{t['border']}"/>
    <text x="139" y="310" text-anchor="middle" class="txt">📍 Melbourne, AU</text>
    <rect x="224" y="290" width="186" height="30" rx="15" fill="{t['chip']}" stroke="{t['border']}"/>
    <circle cx="242" cy="305" r="5" fill="{t['ok']}" class="pulse" style="transform-origin:242px 305px"/>
    <text x="254" y="310" class="txt">Open to contracts</text>
  </g>

  <!-- right: terminal -->
  <rect x="620" y="44" width="532" height="296" rx="12" fill="{t['panel']}" stroke="{t['border']}"/>
  <circle cx="644" cy="66" r="6" fill="#ff5f57"/><circle cx="664" cy="66" r="6" fill="#febc2e"/><circle cx="684" cy="66" r="6" fill="#28c840"/>
  <text x="886" y="71" text-anchor="middle" class="mono mut small">release-candidate · test run</text>
  <line x1="620" y1="86" x2="1152" y2="86" stroke="{t['border']}"/>

  <text x="660" y="116" class="mono"><tspan class="acc">❯</tspan><tspan class="txt"> ./release-gate --env prod</tspan><tspan class="txt cursor"> ▍</tspan></text>
  {''.join(rows)}

  <rect x="660" y="282" width="452" height="4" rx="2" fill="{t['border']}"/>
  <rect x="660" y="282" width="452" height="4" rx="2" fill="{t['ok']}" class="bar"/>

  <g class="final">
    <text x="660" y="318" class="mono mut small">282 checks · 0 blockers</text>
    <g class="pulse">
      <rect x="1004" y="300" width="108" height="28" rx="6" fill="{t['ok']}"/>
      <text x="1058" y="319" text-anchor="middle" class="mono" font-size="14" font-weight="700" fill="{t['bg']}">release: GO</text>
    </g>
  </g>
</svg>
"""


out = Path(__file__).parent
out.mkdir(exist_ok=True)
for name, theme in THEMES.items():
    (out / f"banner-{name}.svg").write_text(svg(theme))
print("wrote", *sorted(p.name for p in out.glob("banner-*.svg")))
