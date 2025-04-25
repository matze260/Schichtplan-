
import streamlit as st
import style_modern
style_modern.set_modern_style()

st.markdown('<div class="welcome-banner">Willkommen in der Schichtplan-App – dein digitaler Dienstplan</div>', unsafe_allow_html=True)
st.title("Schichtplan App - Modern UI")

rolle = st.radio("Login als:", ["Mitarbeiter", "Admin"])

if rolle == "Admin":
    admin_passwort = st.text_input("Admin-Passwort", type="password")
    if admin_passwort == "admin123":
        st.success("Admin eingeloggt.")
        admin_option = st.selectbox("Adminbereich wählen:", ["Übersicht", "Monatsberichte", "Wünsche verwalten", "Nutzerverwaltung"])

        if admin_option == "Übersicht":
            st.markdown("### Admin-Übersicht")
            st.write("Hier findest du eine Übersicht über alle Mitarbeiter, Schichten und Anträge.")
        elif admin_option == "Monatsberichte":
            st.markdown("### Monatsberichte")
            st.write("Hier kannst du Monatsabschlüsse erstellen und als PDF exportieren.")
        elif admin_option == "Wünsche verwalten":
            st.markdown("### Wunsch-/Urlaubsanträge")
            st.write("Hier siehst du alle offenen Anträge und kannst sie genehmigen.")
        elif admin_option == "Nutzerverwaltung":
            st.markdown("### Benutzerverwaltung")
            st.write("Hier kannst du PINs, Rollen und Profile verwalten.")
    elif admin_passwort:
        st.error("Falsches Passwort.")

else:
    benutzername = st.text_input("Benutzername")
    pin = st.text_input("PIN", type="password")
    if benutzername and pin:
        st.success(f"Eingeloggt als {benutzername}")
        st.write("---")
        st.subheader("Beispiel Dienstplan")
        import pandas as pd
        dienstplan = pd.DataFrame({
            "01.05.2025": ["Tag", "Frei", "Nacht"],
            "02.05.2025": ["Nacht", "Tag", "Frei"],
            "03.05.2025": ["Frei", "Tag", "Tag"]
        }, index=["Mitarbeiter_1", "Mitarbeiter_2", "Mitarbeiter_3"])
        st.dataframe(dienstplan)
