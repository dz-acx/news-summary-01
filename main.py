"""main.py writes a fixed summary of world news of 11 November 2026 to /output/entry.txt."""

from pathlib import Path

SUMMARY = """World news, Wednesday 11 November 2026.

Ukraine and Russia ended two days of US-mediated talks in Abu Dhabi by agreeing in principle to the largest prisoner-of-war exchange of the war, with final numbers due Thursday, AP reported; Kyiv rejected a US proposal involving unoccupied Donbas territory. Fighting continued overnight: Ukrainian drones set fire to oil tanks at Russia's Baltic port of Ust-Luga, while Russian strikes hit six major power substations in central Ukraine and a market in Chornomorsk, killing three people.

In Antalya, Turkey, leaders opened speeches at the UN COP31 climate summit, where UN Secretary-General António Guterres warned the world was on a path to destruction; Iran's President Masoud Pezeshkian demanded compensation for environmental damage from US and Israeli strikes, Reuters reported. Saudi Arabia said it intercepted seven Houthi missiles and drones, some aimed at Riyadh, while Israeli strikes and artillery continued in southern Lebanon and Gaza's storm-hit displaced faced flooding and aid restrictions. In Congo, Ebola cases passed 11,000, Reuters reported from government data.

Indonesia's Vice President Gibran Rakabuming Raka handed his resignation to President Prabowo Subianto in Jakarta, Reuters reported, opening a constitutional process for parliament to choose a successor. In Washington, the Republican-led House voted 211-204 to send impeachment articles against Defense Secretary Pete Hegseth to committee, shelving the effort for this Congress, the BBC reported. Democrat Scott Colom won Mississippi's Senate election, AP projected, adding to Democratic gains from the 3 November congressional elections. Brent crude settled up 1.4% at $92.76 a barrel on Iran and Strait of Hormuz uncertainty, and the Nasdaq rose 1.6% as AI shares, led by CoreWeave's 24.7% jump, powered a Wall Street rebound."""


def main() -> None:
    if not (1 <= len(SUMMARY) <= 2000):
        raise SystemExit(f"SUMMARY length {len(SUMMARY)} out of bounds [1, 2000]")
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(SUMMARY, encoding="utf-8")


if __name__ == "__main__":
    main()
