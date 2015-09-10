#! /usr/bin/env python3

ASCII = frozenset(" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~")

# These are the characters that actually occur:

occuring_characters = {
    '%N' : ASCII | frozenset("\xa0\xad°´·ºÁÃ×àáäåèéíîóöøúüĀńőŜσωआटभयर्ṭ’•…∈≤≥⌈⌉ﬀﬁﬂ"),
    '%C' : ASCII | frozenset("¢£§«°±²´·º»½ÁÇ×ÜßàáäåçèéëíîïñòóôõöøùúüýāăćčęěħıłńőřśşšťžΧβγμπρστωϱавдеилмнопрстучшыьяաבוכלᵣᵤḠ\u200b—‘’“”…′ℕ↑⇒∈∏∑∞∩∫≅≈≠≤≥⊂⊆⊗⌈⌉\u3000八發\uf020ﬁﬂ\ufeff𝒩𝓁"),
    '%D' : ASCII | frozenset("\x7f§«°±´¸»ÁÇÉÖ×ÚÜßàáäåçèéêëíîïñóôõöøùúüýăąćČčěłńőŒřŚŞşŠšũūżžǎ́Λλμπϕ\u2002\u2009\u200e‐—’“”…∞∪≡ﬀﬁ"),
    '%H' : ASCII | frozenset("\x81£§©«®°±´µ·»ÁÂÃÅÆÉÕÖ×ÚÜßàáâäåçèéêëíîïñòóôõöøúûüýĀāăćČčěğĭıłńņňőœřśşŠšţūŽžΓΔΛΣΨαβγδζθπστφωϕНРСагдезийклнопрстхчыяאבגדוכלקרשתṭ\u200e—’“”…∏∑√∣≡⌊⌋ﬀﬁﬂ"),
    '%F' : ASCII | frozenset("°²´·ºÁÇ×ÜàáäçèéêíñóôöøúüćńőřşžΓβλ‐‘’”…∞≍≤≥⌈⌉\u3000\ufeff；"),
    '%e' : ASCII | frozenset("¢¨¯°´·×ßáäçèéíôöüīńβλρω\u200b—‘’“”•…∆⊗│："),
    '%p' : ASCII | frozenset("Äéóöø‘’"),
    '%t' : ASCII | frozenset("\x8a®°¹¼×áçèéíñóöúüŠπ…\u2028√≠≤≥\u3000\uf08a\uf0a3\uf0ae\uf0b3\uf0b9"),
    '%o' : ASCII | frozenset("\x8d£«¯´·»Áßáäçèéêíîïðòö÷üπ“”…€←∪≠⊤⌊⌿⍳⍴⍸○"),
    '%Y' : ASCII | frozenset("ßáéñöøńőΧ’…⊂\u3000"),
    '%A' : ASCII | frozenset("ÁÅÆÇÉØÜßàáâäçèéëíñóôöøúüČńņőşš"),
    '%E' : ASCII | frozenset("´ÁÉßàáãäçèéíñóôöøüýčěłńőš’"),
}

# These are the characters that are acceotable:

acceptable_characters = {
    '%N' : ASCII | frozenset("\xa0\xad°´·ºÁÃ×àáäåèéíîóöøúüĀńőŜσωआटभयर्ṭ’•…∈≤≥⌈⌉"),
    '%C' : ASCII | frozenset("¢£§«°±²´·º»½ÁÇ×ÜßàáäåçèéëíîïñòóôõöøùúüýāăćčęěħıłńőřśşšťžΧβγμπρστωϱавдеилмнопрстучшыьяաבוכלᵣᵤḠ\u200b—‘’“”…′ℕ↑⇒∈∏∑∞∩∫≅≈≠≤≥⊂⊆⊗⌈⌉\u3000八發\uf020ﬁﬂ\ufeff𝒩𝓁"),
    '%D' : ASCII | frozenset("\x7f§«°±´¸»ÁÇÉÖ×ÚÜßàáäåçèéêëíîïñóôõöøùúüýăąćČčěłńőŒřŚŞşŠšũūżžǎ́Λλμπϕ\u2002\u2009\u200e‐—’“”…∞∪≡"),
    '%H' : ASCII | frozenset("\x81£§©«®°±´µ·»ÁÂÃÅÆÉÕÖ×ÚÜßàáâäåçèéêëíîïñòóôõöøúûüýĀāăćČčěğĭıłńņňőœřśşŠšţūŽžΓΔΛΣΨαβγδζθπστφωϕНРСагдезийклнопрстхчыяאבגדוכלקרשתṭ\u200e—’“”…∏∑√∣≡⌊⌋"),
    '%F' : ASCII | frozenset("°²´·ºÁÇ×ÜàáäçèéêíñóôöøúüćńőřşžΓβλ‐‘’”…∞≍≤≥⌈⌉\u3000\ufeff；"),
    '%e' : ASCII | frozenset("¢¨¯°´·×ßáäçèéíôöüīńβλρω\u200b—‘’“”•…∆⊗│："),
    '%p' : ASCII | frozenset("Äéóöø‘’"),
    '%t' : ASCII | frozenset("\x8a®°¹¼×áçèéíñóöúüŠπ…\u2028√≠≤≥\u3000\uf08a\uf0a3\uf0ae\uf0b3\uf0b9"),
    '%o' : ASCII | frozenset("\x8d£«¯´·»Áßáäçèéêíîïðòö÷üπ“”…€←∪≠⊤⌊⌿⍳⍴⍸○"),
    '%Y' : ASCII | frozenset("ßáéñöøńőΧ’…⊂\u3000"),
    '%A' : ASCII | frozenset("ÁÅÆÇÉØÜßàáâäçèéëíñóôöøúüČńņőşš"),
    '%E' : ASCII | frozenset("´ÁÉßàáãäçèéíñóôöøüýčěłńőš’"),
}

def nasty(s):
    nasties = ASCII - set(s)
    nasties = sorted(nasties)
    nasties = ", ".join(["{!r}".format(c) for c in nasties])
    return nasties
