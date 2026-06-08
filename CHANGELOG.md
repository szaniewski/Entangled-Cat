# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- **Card Recycling After Measurement (Game Economy Update):** All cards (Algorithms, Gates, and Special cards) involved in a Measurement—whether successful or failed—are now immediately sent to the global Discard Pile. Players no longer keep physical cards to represent points; instead, they track scores using external methods (pen and paper, digital tracker, or custom tokens). This ensures continuous circulation of the 100-card deck and prevents card lockout.
- **Deck Depletion & Discard Pile Rule:** If the main draw deck is exhausted before the end of the game, the entire Discard Pile is shuffled to form a new draw deck. This maintains gameplay flow and ensures no dead states.
- **Once-Per-Turn Card Swap Mechanic (Quantum Fluctuation):** Players may now perform exactly one Card Swap action per turn during their Action Phase. Players discard exactly 2 cards to the global Discard Pile and immediately draw 2 new cards from the main draw deck, followed by a thorough deck reshuffling. This action prevents hand deadlock and adds tactical depth.
- **FAQ Entry:** Added clarification that Card Swap counts as a free action but is limited to once per turn.

### Changed
- **Measurement Results Section:** Updated to reflect that all cards are discarded to the global Discard Pile regardless of success or failure, with points recorded instantly before discard.
- **Scoring Emphasis:** Clarified that points represent accumulated value tracked externally, not physical card possession.

### Initial project scaffold
