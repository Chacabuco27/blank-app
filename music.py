# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# streamlit run your_script.py
# python -m streamlit run music.py

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import random

# Cargar archivo
df = pd.read_csv("artistas.csv")

# Corregir nombre de columna con espacio extra
df.rename(columns={"artista _musical": "artista_musical"}, inplace=True)

# st.sidebar.image("nombre del logo", use_container_width=True)

with st.sidebar:
    # Mostrar logo encima del menú
    st.image("logo_ori.png", use_container_width=True)

    # Menú de navegación
    selected = option_menu(
        menu_title=None,  
        options=["Inicio", 'Descubre', 'Tendencias', 'Géneros', 'Aportes'],
        icons=['house', 'search', 'fire', 'music-note-list', 'envelope'],
        default_index=0
    )
    
if selected == "Inicio":
    st.image("logo.png", width=700)
    
    st.markdown("""
    <div style='text-align: justify; font-size: 20px;'>
    <p>¡Bienvenido a un viaje sonoro por Ecos del Perú! Esta página es un homenaje vibrante a la música peruana en toda su diversidad, desde las montañas hasta la selva y las ciudades costeras. Aquí encontrarás una exploración profunda de un aproximado de más de diez géneros que han marcado la identidad del país: desde la energía contagiante del rock y la cumbia, hasta la fuerza ancestral de la música andina y la modernidad del urbano y el hip hop.</p>
    <p>Pero no solo hablamos de estilos, también celebramos a quienes los hacen posibles. Navega por las historias de leyendas consagradas y descubre a talentos emergentes que están transformando la escena nacional. Encontrarás perfiles de artistas, sus trayectorias, y el impacto social que han generado a través de la música. Esta es más que una página, es una ventana abierta a los sonidos que nos definen como país.</p>
    </div>
    """, unsafe_allow_html=True)

    st.header('🎼 Géneros Musicales Peruanos')

    with st.expander('Rock'):
        st.write('El rock peruano surgió en los años 60, influenciado por el beat británico y el rock psicodélico estadounidense...')
        st.image('rock_peruano.jpg', width=700)

    with st.expander('Chicha'):
        st.write('La chicha nació en los años 70 como una fusión entre la cumbia colombiana, el rock psicodélico y los ritmos andinos...')
        st.image('chicha.jpg', width=700)

    with st.expander('Salsa'):
        st.write('La salsa en el Perú se popularizó en los años 70, influenciada por el boom salsero de Nueva York y el Caribe...')
        st.image('salsa.png', width=700)

    with st.expander('Cumbia'):
        st.write('La cumbia peruana emergió en los años 60 como una adaptación local de la cumbia colombiana...')
        st.image('cumbia.jpg', width=700)

    with st.expander('Hip Hop'):
        st.write('El hip hop en el Perú nació en los años 90 como una expresión de las juventudes urbanas...')
        st.image('hiphop.jpg', width=500)

    with st.expander('Urbano'):
        st.write('La música urbana en el Perú tomó fuerza en los años 2000, influenciada por el reguetón, el trap y otros ritmos latinos...')
        st.image('urbano.png', width=700)

    with st.expander('Andino'):
        st.write('La música andina en el Perú tiene raíces ancestrales que se remontan a las civilizaciones prehispánicas...')
        st.image('andina.jpg', width=700)

    with st.expander('Pop'):
        st.write('El pop peruano comenzó a consolidarse en las décadas de 1980 y 1990, influenciado por las corrientes del pop latino y anglosajón...')
        st.image('pop.png', width=700)

    with st.expander('Criollo'):
        st.write('La música criolla es uno de los pilares de la identidad cultural peruana, con raíces en la costa...')
        st.image('criolla.jpg', width=700)

elif selected == "Descubre":
    elección = ['artista_musical', 'biografía', 'Link_información', 'url_imagen', 'género_musical',
                'audiencia_Spotify', 'canción_más_escuchada', 'reproducciones', 'url_video']
    artista_random = df[elección].sample(1).iloc[0]

    st.subheader("🎤 Artista aleatorio:")
    st.markdown(f"""<div style="text-align: center;">
        <img src="{artista_random['url_imagen']}" width="500" />
        <p style="font-weight: bold;">{artista_random['artista_musical']}</p></div>""",
        unsafe_allow_html=True)
    
    # Crear columnas
    col1, col2 = st.columns([1, 2])  # Ancho relativo (imagen más angosta, info más ancha)

    # Columna 1: imagen
    with col1:
        st.markdown(f"**🎶 Nombre:** {artista_random['artista_musical']}")
        st.markdown(f"**🎧 Género:** {artista_random['género_musical']}")
        st.markdown(f"**🌍 Audiencia en Spotify:** {artista_random['audiencia_Spotify']}")
        st.markdown(f"[🔗 Más información]({artista_random['Link_información']})")
        st.markdown(f"[🎬 Ver video]({artista_random['url_video']})")
    # Columna 2: información textual
    with col2:
        st.markdown(f"<div style='text-align: justify; font-size: 15px;'><strong>📝 Biografía:</strong> {artista_random['biografía']}</div>",
        unsafe_allow_html=True)
        st.markdown(f"**🔥 Canción más escuchada:** {artista_random['canción_más_escuchada']} ({artista_random['reproducciones']} reproducciones)")

elif selected == "Tendencias":
    # Función para convertir audiencia tipo '3.2M' o '850K' a número real
    def convertir_audiencia(valor):
        if pd.isna(valor):
            return 0
        if isinstance(valor, str):
            valor = valor.strip()
            if 'M' in valor:
                return float(valor.replace('M', '')) * 1_000_000
            elif 'k' in valor:
                return float(valor.replace('k', '')) * 1_000
            else:
                try:
                    return float(valor)
                except ValueError:
                    return 0
        try:
            return float(valor)
        except:
            return 0

    # Convertimos la columna de audiencia
    df['audiencia_convertida'] = df['audiencia_Spotify'].apply(convertir_audiencia)

    # Ordenamos por audiencia y tomamos los 10 más altos
    top_10 = df.sort_values(by='audiencia_convertida', ascending=False).head(10)

    # Agregamos columna Ranking
    top_10['Ranking'] = range(1, len(top_10) + 1)

    # Quitamos el índice original para que no se muestre
    top_10 = top_10.reset_index(drop=True)

    # Mostramos la tabla con ranking
    st.subheader("🔥 Top Artistas en Tendencia")

# Recorremos cada artista del Top 10
    for index, row in top_10.iterrows():
        # Dividimos en 2 columnas: imagen | info
        col1, col2 = st.columns([1.2, 3])

        with col1:
            # Imagen más grande
            st.image(row['url_imagen'], width=160)

        with col2:
            # Nombre del artista con ranking
            st.markdown(f"### {row['Ranking']}. {row['artista_musical']}")
            # Audiencia visual
            st.markdown(f"🎧 Audiencia: {row['audiencia_Spotify']}")

elif selected == "Géneros":
    st.subheader("🎶 Explora artistas por género musical")

    # Diccionario de imágenes por género
    imagenes_genero = {
        'Andino': 'andina.jpg',
        'Chicha': 'chicha.jpg',
        'Criollo': 'criolla.jpg',
        'Cumbia': 'cumbia.jpg',
        'Electrónica': 'electronica.jpeg',
        'Fusión': 'fusion.jpeg',
        'Hip hop': 'hiphop.jpg',
        'Humor/Viral': 'humor.jpeg',
        'Parodia': 'parodia.jpeg',
        'Pop': 'pop.png',
        'Reggae/Funk': 'reggae.jpeg',
        'Rock': 'rock_peruano.jpg',
        'Salsa': 'salsa.png',
        'Tecnocumbia': 'tecnocumbia.png',
        'Urbano': 'urbano.png',
    }

    lista_generos = list(imagenes_genero.keys())

    # Estado de selección
    if "genero_elegido" not in st.session_state:
        st.session_state.genero_elegido = None

    # Mostrar botones si no se ha elegido un género
    if st.session_state.genero_elegido is None:
        st.markdown("Selecciona un género musical:")
        cols = st.columns(4)
        for i, genero in enumerate(lista_generos):
            col = cols[i % 4]
            with col:
                st.image(imagenes_genero[genero], use_container_width=True)
                if st.button(f"{genero}", key=genero):
                    st.session_state.genero_elegido = genero
                    st.rerun()

    # Mostrar artistas si ya se eligió un género
    else:
        genero = st.session_state.genero_elegido
        st.markdown(f"### 🎧 Artistas del género: {genero}")

        df_filtrado = df[df['género_musical'].str.contains(genero, case=False, na=False)]

        if df_filtrado.empty:
            st.warning("No se encontraron artistas con ese género.")
        else:
            for index, row in df_filtrado.iterrows():
                col1, col2 = st.columns([1.2, 3])
                with col1:
                    st.image(row['url_imagen'], use_container_width=True)
                with col2:
                    st.markdown(f"### {row['artista_musical']}")
                    st.markdown(f"🎧 Audiencia: {row['audiencia_Spotify']}")
                    st.markdown(f"🎵 Género: {row['género_musical']}")

        st.markdown("---")
        if st.button("🔙 Volver a géneros"):
            st.session_state.genero_elegido = None
            st.rerun()

elif selected == "Aportes":
    st.title("📬 Aporta un artista a Ecos del Perú")

    st.markdown("¿Conoces un artista peruano que deba estar aquí? ¡Compártenos su información!")

    if "aporte_enviado" not in st.session_state:
        st.session_state.aporte_enviado = False

    if not st.session_state.aporte_enviado:
        with st.form("form_aporte"):
            nombre = st.text_input("🎤 Nombre del artista")
            url_imagen = st.text_input("🖼️ URL de la imagen")
            biografia = st.text_area("📖 Biografía del artista")
            audiencia = st.text_input("👥 Audiencia mensual en Spotify (ej: 3.2M o 120K)")
            cancion_mas_escuchada = st.text_input("🎧 Canción más escuchada")
            link_cancion = st.text_input("🔗 Link de la canción en Spotify")
            vistas_cancion = st.text_input("📈 Visualizaciones/reproducciones de la canción")

            submit = st.form_submit_button("Enviar aporte")

        if submit:
            if all([
                nombre.strip(),
                url_imagen.strip(),
                biografia.strip(),
                audiencia.strip(),
                cancion_mas_escuchada.strip(),
                link_cancion.strip(),
                vistas_cancion.strip()
            ]):
                nuevo = {
                    "artista_musical": nombre,
                    "url_imagen": url_imagen,
                    "biografía": biografia,
                    "audiencia_Spotify": audiencia,
                    "canción_más_escuchada": cancion_mas_escuchada,
                    "url_video": link_cancion,
                    "reproducciones": vistas_cancion
                }

                try:
                    df_aportes = pd.read_csv("aportes.csv")
                except FileNotFoundError:
                    df_aportes = pd.DataFrame(columns=nuevo.keys())

                df_aportes = pd.concat([df_aportes, pd.DataFrame([nuevo])], ignore_index=True)
                df_aportes.to_csv("aportes.csv", index=False)

                st.session_state.aporte_enviado = True
                st.rerun()
            else:
                st.error("Por favor, completa **todos los campos** antes de enviar el aporte.")
    else:
        st.success("¡Gracias por tu aporte! El artista ha sido registrado correctamente. 🙌")
