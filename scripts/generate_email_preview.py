"""Generate a rich preview of the Daily arXiv Dispatch email.

Builds 10 mock Paper objects across 4 categories with a mix of score bands,
code links, special characters, and one >600-char abstract, then writes the
rendered HTML to ``logs/email_preview.html`` for visual verification.

Run:
    python scripts/generate_email_preview.py
"""

from __future__ import annotations

import os
from datetime import date
from typing import List

from src.daily_arxiv.models.paper import Paper
from src.daily_arxiv.services.email_service import EmailService


def _paper(  # noqa: PLR0913 — fixture builder, simple kwargs are fine here.
    key: str,
    title: str,
    authors: str,
    abstract: str,
    score: float,
    code_url: str | None,
    category: str,
    published: date = date(2025, 6, 17),
) -> Paper:
    return Paper(
        paper_key=key,
        title=title,
        authors_str=authors,
        abstract=abstract,
        published=published,
        updated=published,
        primary_category="cs.GR",
        all_categories=["cs.GR", "cs.HC"],
        entry_id=f"http://arxiv.org/abs/{key}",
        abs_url=f"http://arxiv.org/abs/{key}",
        code_url=code_url,
        category=category,
        score=score,
        matched_keywords=["motion", "world model"],
    )


def build_papers() -> dict[str, List[Paper]]:
    long_abstract = (
        "We present MotionSmith, a unified framework for authoring "
        "character motion across multiple modalities. Our approach "
        "combines kinematic editing with physics-based refinement, "
        "enabling animators to iterate rapidly on motion sketches while "
        "preserving physical plausibility. The system introduces a novel "
        "motion representation that decouples high-level intent from "
        "low-level joint trajectories, allowing users to specify motion "
        "via sketches, mocap clips, or natural language descriptions. "
        "We evaluate MotionSmith on a benchmark of 240 motion sequences "
        "spanning locomotion, interaction, and expressive gesture. "
        "Quantitative results show that our physics refinement step "
        "reduces foot skating by 78% and inter-penetration by 62% "
        "relative to the baseline, while user study participants rated "
        "MotionSmith-authored clips as more natural than the comparison "
        "systems in 81% of trials. The full evaluation methodology, "
        "additional ablations, and failure case analyses are reported in "
        "the supplementary material, along with a discussion of ethical "
        "considerations around synthetic motion generation. This is a "
        "deliberately long abstract that exceeds the 600-character trim "
        "limit so that the Dispatch renderer's trimming logic is "
        "exercised by the preview."
    )

    return {
        "Character Motion": [
            _paper(
                "2506.14513",
                "MotionSmith: A <Unified> Framework for Authoring & Editing Motion",
                "Alan Synn",
                long_abstract,
                0.82,
                "https://github.com/AlanSynn/motionsmith",
                "Character Motion",
            ),
            _paper(
                "2506.14042",
                "Neural Motion Fields for Real-Time Character Synthesis",
                "Maria Gonzalez",
                "We introduce a compact neural representation for character "
                "motion that supports interactive editing and playback.",
                0.65,
                None,
                "Character Motion",
            ),
            _paper(
                "2506.13987",
                "Physics-Based Avatar Locomotion in Uneven Terrain",
                "Kenji Tanaka",
                "A learned controller for humanoid avatars traversing "
                "irregular terrain with robust balance recovery.",
                0.45,
                "https://github.com/example/avatar-locomotion",
                "Character Motion",
            ),
        ],
        "World Models": [
            _paper(
                "2506.14000",
                "World Models for Robots: A Survey & Open Challenges",
                "Jane Doe",
                "We survey recent advances in learned world models for "
                "robotic control and outline open challenges.",
                0.61,
                "https://github.com/x/y",
                "World Models",
            ),
            _paper(
                "2506.13771",
                "Generative Interactive <Video> at Scale",
                "Ravi Patel",
                "Scaling interactive video generation to hour-length "
                "rollouts with consistent scene dynamics.",
                0.32,
                None,
                "World Models",
            ),
        ],
        "Generative Models": [
            _paper(
                "2506.13550",
                "Diffusion Transformers at Frontier Scale",
                "Yuki Watanabe",
                "Training recipes and architecture choices for "
                "billion-parameter diffusion transformers.",
                0.55,
                "https://github.com/example/dit-scale",
                "Generative Models",
            ),
            _paper(
                "2506.13301",
                "Flow Matching for Fast & High-Fidelity Generation",
                "Olivia Chen",
                "Continuous-time flow matching reduces sampling cost "
                "while preserving sample quality.",
                0.28,
                None,
                "Generative Models",
            ),
            _paper(
                "2506.13190",
                "Consistency Models Revisited: Trade-offs & Limits",
                "Sara Müller",
                "Re-examining consistency model theory and where the "
                "few-step regime breaks down.",
                0.18,
                None,
                "Generative Models",
            ),
        ],
        "Human-Computer Interaction": [
            _paper(
                "2506.12999",
                "Brain-Computer Interfaces & <Accessibility> in VR",
                "Liam O'Connor",
                "An accessibility-first BCI pipeline for immersive VR "
                "with sub-100ms intent decoding.",
                0.42,
                "https://github.com/example/a11y-bci",
                "Human-Computer Interaction",
            ),
            _paper(
                "2506.12780",
                "Haptic Feedback for VR/AR Surgical Training",
                "Wei Zhang",
                "Wearable haptic gloves improve surgical skill transfer "
                "in VR training modules.",
                0.15,
                None,
                "Human-Computer Interaction",
            ),
        ],
    }


def main() -> int:
    papers_by_cat = build_papers()
    stats = {
        "total": sum(len(v) for v in papers_by_cat.values()),
        "categories": sum(1 for v in papers_by_cat.values() if v),
        "threshold": 0.15,
    }

    service = EmailService({"email_settings": {"enabled": True}})
    html = service.render_email(papers_by_cat, "2025-06-17", stats)

    out_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "email_preview.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Wrote {out_path} ({len(html)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
