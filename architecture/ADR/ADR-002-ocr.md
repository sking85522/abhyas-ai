# ADR-002: OCR Engine Selection
**Context**: Processing various qualities of images and handwriting.
**Decision**: Implement a dual-engine strategy using Tesseract for standard text and EasyOCR for complex/handwritten segments. Abstract behind an internal interface.
