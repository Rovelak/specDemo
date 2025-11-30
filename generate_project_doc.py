#!/usr/bin/env python3
"""
Generate a DOCX file containing project description from CLAUDE.md
"""

import os
import zipfile
import datetime

def create_docx(output_path):
    """Create a DOCX file with project description"""

    # Create DOCX structure
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as docx:
        # [Content_Types].xml
        content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
</Types>'''
        docx.writestr('[Content_Types].xml', content_types)

        # _rels/.rels
        rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''
        docx.writestr('_rels/.rels', rels)

        # word/_rels/document.xml.rels
        doc_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
</Relationships>'''
        docx.writestr('word/_rels/document.xml.rels', doc_rels)

        # word/styles.xml
        styles = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
        <w:sz w:val="22"/>
      </w:rPr>
    </w:rPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:qFormat/>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Title">
    <w:name w:val="Title"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:pPr>
      <w:spacing w:before="240" w:after="240"/>
      <w:jc w:val="center"/>
    </w:pPr>
    <w:rPr>
      <w:b/>
      <w:sz w:val="56"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="Heading 1"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:pPr>
      <w:spacing w:before="480" w:after="120"/>
    </w:pPr>
    <w:rPr>
      <w:b/>
      <w:sz w:val="32"/>
      <w:color w:val="2E75B5"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="Heading 2"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:pPr>
      <w:spacing w:before="360" w:after="120"/>
    </w:pPr>
    <w:rPr>
      <w:b/>
      <w:sz w:val="28"/>
      <w:color w:val="2E75B5"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading3">
    <w:name w:val="Heading 3"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:pPr>
      <w:spacing w:before="240" w:after="120"/>
    </w:pPr>
    <w:rPr>
      <w:b/>
      <w:sz w:val="24"/>
      <w:color w:val="2E75B5"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="ListParagraph">
    <w:name w:val="List Paragraph"/>
    <w:basedOn w:val="Normal"/>
    <w:pPr>
      <w:ind w:left="720"/>
    </w:pPr>
  </w:style>
  <w:style w:type="character" w:styleId="CodeChar">
    <w:name w:val="Code"/>
    <w:rPr>
      <w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/>
      <w:color w:val="C7254E"/>
      <w:shd w:val="clear" w:color="auto" w:fill="F9F2F4"/>
    </w:rPr>
  </w:style>
</w:styles>'''
        docx.writestr('word/styles.xml', styles)

        # word/numbering.xml
        numbering = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:abstractNum w:abstractNumId="0">
    <w:multiLevelType w:val="hybridMultilevel"/>
    <w:lvl w:ilvl="0">
      <w:start w:val="1"/>
      <w:numFmt w:val="decimal"/>
      <w:lvlText w:val="%1."/>
      <w:lvlJc w:val="left"/>
      <w:pPr>
        <w:ind w:left="720" w:hanging="360"/>
      </w:pPr>
    </w:lvl>
  </w:abstractNum>
  <w:abstractNum w:abstractNumId="1">
    <w:multiLevelType w:val="hybridMultilevel"/>
    <w:lvl w:ilvl="0">
      <w:start w:val="1"/>
      <w:numFmt w:val="bullet"/>
      <w:lvlText w:val="•"/>
      <w:lvlJc w:val="left"/>
      <w:pPr>
        <w:ind w:left="720" w:hanging="360"/>
      </w:pPr>
    </w:lvl>
  </w:abstractNum>
  <w:num w:numId="1">
    <w:abstractNumId w:val="0"/>
  </w:num>
  <w:num w:numId="2">
    <w:abstractNumId w:val="1"/>
  </w:num>
</w:numbering>'''
        docx.writestr('word/numbering.xml', numbering)

        # word/document.xml with project content
        document = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
            xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <w:body>

    <!-- Title -->
    <w:p>
      <w:pPr><w:pStyle w:val="Title"/></w:pPr>
      <w:r><w:t>Project Documentation</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:spacing w:after="240"/>
        <w:jc w:val="center"/>
      </w:pPr>
      <w:r>
        <w:rPr><w:i/></w:rPr>
        <w:t>Next.js Movie Review Website</w:t>
      </w:r>
    </w:p>

    <!-- Project Overview -->
    <w:p>
      <w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
      <w:r><w:t>Project Overview</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr><w:spacing w:after="120"/></w:pPr>
      <w:r><w:t>This is a </w:t></w:r>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Next.js movie review website</w:t></w:r>
      <w:r><w:t> built from a Specify template. The project uses </w:t></w:r>
      <w:r><w:rPr><w:b/></w:rPr><w:t>static mock data</w:t></w:r>
      <w:r><w:t> (no backend/API) and implements a landing page with movie listings and individual movie detail pages. The codebase is structured with specifications in </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>specs/</w:t></w:r>
      <w:r><w:t> and a frontend-only implementation.</w:t></w:r>
    </w:p>

    <!-- Development Commands -->
    <w:p>
      <w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
      <w:r><w:t>Development Commands</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr><w:spacing w:after="120"/></w:pPr>
      <w:r><w:t>All commands are run from the </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>frontend/</w:t></w:r>
      <w:r><w:t> directory:</w:t></w:r>
    </w:p>

    <!-- Command list -->
    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>npm run dev</w:t></w:r>
      <w:r><w:t> - Development server (runs on localhost:3000)</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>npm run build</w:t></w:r>
      <w:r><w:t> - Production build</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>npm run start</w:t></w:r>
      <w:r><w:t> - Start production server</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>npm run lint</w:t></w:r>
      <w:r><w:t> - Run linting</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>npm test</w:t></w:r>
      <w:r><w:t> - Run Jest unit tests</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="240"/>
      </w:pPr>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>npm run test:e2e</w:t></w:r>
      <w:r><w:t> - Run Playwright E2E tests (auto-starts dev server)</w:t></w:r>
    </w:p>

    <!-- Architecture -->
    <w:p>
      <w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
      <w:r><w:t>Architecture</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr><w:pStyle w:val="Heading2"/></w:pPr>
      <w:r><w:t>Data Flow</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr><w:spacing w:after="120"/></w:pPr>
      <w:r><w:t>The application uses a </w:t></w:r>
      <w:r><w:rPr><w:b/></w:rPr><w:t>fixture-based data architecture</w:t></w:r>
      <w:r><w:t> with no external API:</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Source of truth:</w:t></w:r>
      <w:r><w:t> </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>frontend/fixtures/movies.json</w:t></w:r>
      <w:r><w:t> contains all movie data</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Data loader:</w:t></w:r>
      <w:r><w:t> </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>frontend/src/lib/fixtures.ts</w:t></w:r>
      <w:r><w:t> loads and validates fixture data</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Type safety:</w:t></w:r>
      <w:r><w:t> </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>frontend/src/types/models.ts</w:t></w:r>
      <w:r><w:t> defines Movie and Review types</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
        <w:spacing w:after="240"/>
      </w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Validation:</w:t></w:r>
      <w:r><w:t> The fixtures module includes runtime validation (</w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>validateMoviesFixture()</w:t></w:r>
      <w:r><w:t>) that checks data integrity on load</w:t></w:r>
    </w:p>

    <!-- Key Architectural Patterns -->
    <w:p>
      <w:pPr><w:pStyle w:val="Heading2"/></w:pPr>
      <w:r><w:t>Key Architectural Patterns</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr><w:spacing w:after="120"/></w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Pages Router:</w:t></w:r>
      <w:r><w:t> Uses Next.js Pages Router (not App Router)</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>Landing: </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>src/pages/index.tsx</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>Movie detail: </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>src/pages/movies/[id].tsx</w:t></w:r>
      <w:r><w:t> (dynamic route)</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="120"/>
      </w:pPr>
      <w:r><w:t>App wrapper: </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>src/pages/_app.tsx</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr><w:spacing w:after="120"/></w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Component Structure:</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>Presentational components in </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>src/components/</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>shadcn/ui components in </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>src/components/ui/</w:t></w:r>
      <w:r><w:t> (Tailwind-based)</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="120"/>
      </w:pPr>
      <w:r><w:t>Layout wrapper: </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>src/components/Layout.tsx</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr><w:spacing w:after="120"/></w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Styling:</w:t></w:r>
      <w:r><w:t> Tailwind CSS with shadcn/ui design system</w:t></w:r>
    </w:p>

    <!-- Page break before Testing Strategy -->
    <w:p>
      <w:r><w:br w:type="page"/></w:r>
    </w:p>

    <!-- Testing Strategy -->
    <w:p>
      <w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
      <w:r><w:t>Testing Strategy</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr><w:pStyle w:val="Heading2"/></w:pPr>
      <w:r><w:t>Unit Tests (Jest)</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>Config: </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>jest.config.js</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>Setup: </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>tests/setupTests.ts</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>Test files colocated with source: </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>src/tests/</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="240"/>
      </w:pPr>
      <w:r><w:t>Uses </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>@testing-library/react</w:t></w:r>
      <w:r><w:t> and </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>@testing-library/jest-dom</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr><w:pStyle w:val="Heading2"/></w:pPr>
      <w:r><w:t>E2E Tests (Playwright)</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>Config: </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>playwright.config.ts</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>Test directory: </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>tests/e2e/</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>Automatically starts dev server on port 3000</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>Retries failed tests once</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="240"/>
      </w:pPr>
      <w:r><w:t>Generates traces on first retry</w:t></w:r>
    </w:p>

    <!-- Specify Integration -->
    <w:p>
      <w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
      <w:r><w:t>Specify Integration</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr><w:spacing w:after="120"/></w:pPr>
      <w:r><w:t>This project was built from a Specify template and uses specification-driven development:</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Specs location:</w:t></w:r>
      <w:r><w:t> </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>specs/001-i-am-building/</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Active spec:</w:t></w:r>
      <w:r><w:t> </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>spec.md</w:t></w:r>
      <w:r><w:t> defines user stories, requirements, and acceptance criteria</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Supporting docs:</w:t></w:r>
      <w:r><w:t> </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>plan.md, tasks.md, test-plan.md, security.md, a11y-report.md</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="240"/>
      </w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Copilot guidance:</w:t></w:r>
      <w:r><w:t> </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>.github/copilot-instructions.md</w:t></w:r>
      <w:r><w:t> (auto-generated from feature plans)</w:t></w:r>
    </w:p>

    <!-- Important Constraints -->
    <w:p>
      <w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
      <w:r><w:t>Important Constraints</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>No backend:</w:t></w:r>
      <w:r><w:t> All data comes from </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>fixtures/movies.json</w:t></w:r>
      <w:r><w:t> - do not attempt to fetch from external APIs</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Node.js 22+:</w:t></w:r>
      <w:r><w:t> Locked via </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>.nvmrc</w:t></w:r>
      <w:r><w:t> and </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>engines</w:t></w:r>
      <w:r><w:t> in </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>package.json</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Static export compatibility:</w:t></w:r>
      <w:r><w:t> Next.js config should support static export (no server-side runtime dependencies)</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
        <w:spacing w:after="240"/>
      </w:pPr>
      <w:r><w:rPr><w:b/></w:rPr><w:t>Fixture validation:</w:t></w:r>
      <w:r><w:t> When modifying movie data structure, update both </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>types/models.ts</w:t></w:r>
      <w:r><w:t> and </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>lib/fixtures.ts</w:t></w:r>
      <w:r><w:t> validation logic</w:t></w:r>
    </w:p>

    <!-- Working with Movie Data -->
    <w:p>
      <w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
      <w:r><w:t>Working with Movie Data</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr><w:spacing w:after="120"/></w:pPr>
      <w:r><w:t>To modify the movie dataset:</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>Edit </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>frontend/fixtures/movies.json</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>Ensure data matches the </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>Movie</w:t></w:r>
      <w:r><w:t> type in </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>src/types/models.ts</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>Run </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>npm run dev</w:t></w:r>
      <w:r><w:t> and check console for validation errors from </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>validateMoviesFixture()</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
        <w:spacing w:after="60"/>
      </w:pPr>
      <w:r><w:t>If adding new fields, update:</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
        <w:ind w:left="1440" w:hanging="360"/>
      </w:pPr>
      <w:r><w:t>Type definitions in </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>src/types/models.ts</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="60"/>
        <w:ind w:left="1440" w:hanging="360"/>
      </w:pPr>
      <w:r><w:t>Validation logic in </w:t></w:r>
      <w:r><w:rPr><w:rStyle w:val="CodeChar"/></w:rPr><w:t>src/lib/fixtures.ts</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr>
        <w:pStyle w:val="ListParagraph"/>
        <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
        <w:spacing w:after="240"/>
        <w:ind w:left="1440" w:hanging="360"/>
      </w:pPr>
      <w:r><w:t>Relevant components that display the data</w:t></w:r>
    </w:p>

    <!-- Footer -->
    <w:p>
      <w:pPr>
        <w:spacing w:before="480"/>
        <w:jc w:val="center"/>
      </w:pPr>
      <w:r>
        <w:rPr><w:i/><w:sz w:val="18"/></w:rPr>
        <w:t>Generated from CLAUDE.md - </w:t>
      </w:r>
      <w:r>
        <w:rPr><w:i/><w:sz w:val="18"/></w:rPr>
        <w:t>''' + datetime.datetime.now().strftime("%B %d, %Y") + '''</w:t>
      </w:r>
    </w:p>

    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720"/>
    </w:sectPr>
  </w:body>
</w:document>'''
        docx.writestr('word/document.xml', document)

    print(f"DOCX file created successfully: {output_path}")

if __name__ == "__main__":
    output_file = "Project_Documentation.docx"
    create_docx(output_file)
