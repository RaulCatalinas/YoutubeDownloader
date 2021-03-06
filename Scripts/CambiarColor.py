class CambiarColor:
    @staticmethod
    def FuncionCambiarColor(button, colorRatonDentro, colorRatonFuera):
        """
        Toma un botón y dos colores, y vincula el botón para cambiar de color cuando el mouse ingresa y deja el botón
        @param button - El botón al que desea cambiar el color.
        @param colorRatonDentro - El color del botón cuando el mouse está sobre él.
        @param colorRatonFuera - El color del botón cuando el mouse no está sobre él.
        """
        button.bind(
            "<Enter>",
            func=lambda e: button.config(background=colorRatonDentro, cursor="hand2"),
        )

        button.bind("<Leave>", func=lambda e: button.config(background=colorRatonFuera))
