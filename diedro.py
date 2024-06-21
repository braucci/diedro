import numpy as np
import matplotlib.pyplot as plt

# Autore : Raucci Biagio
# Data   : 2021-06-01
# Scopo  : Mostrare graficamente l'effetto del diedro sulle ali di un aereo


def plot_wings_with_dihedral_and_lift_vectors_complete_final_adjusted():
    # Lunghezza dei segmenti
    segment_length = 10
    # Angoli di diedro in gradi
    dihedral_angle_3 = 3
    dihedral_angle_6 = 6
    # Calcolo degli angoli in radianti
    dihedral_radians_3 = np.deg2rad(dihedral_angle_3)
    dihedral_radians_6 = np.deg2rad(dihedral_angle_6)
    
    # Creazione della figura e dei subplot
    fig, axs = plt.subplots(2, 2, figsize=(14, 12))
    fig.subplots_adjust(hspace=0.5, wspace=0.3)

    # Segmenti orizzontali senza diedro
    x1, y1 = np.array([-segment_length/2, segment_length/2]), np.array([0, 0])
    axs[0, 0].plot(x1, y1, 'k-', linewidth=2)
    axs[0, 0].quiver(-segment_length/4, 0, 0, 4, angles='xy', scale_units='xy', scale=1, color='b')
    axs[0, 0].quiver(segment_length/4, 0, 0, 4, angles='xy', scale_units='xy', scale=1, color='b')
    axs[0, 0].set_aspect('equal')
    axs[0, 0].grid(True)
    axs[0, 0].set_xlim(-segment_length, segment_length)
    axs[0, 0].set_ylim(-4, 6)
    axs[0, 0].set_title('Segmenti affiancati con vettori di portanza')
    axs[0, 0].text(-segment_length/4, 4.5, 'Portanza Destra', ha='center')
    axs[0, 0].text(segment_length/4, 4.5, 'Portanza Sinistra', ha='center')
    axs[0, 0].set_xlabel('Direzione di volo')

    # Segmenti con diedro di 3°
    x2_left = np.array([-segment_length/2, 0])
    y2_left = np.tan(-dihedral_radians_3) * x2_left  # Calcolo della posizione Y con diedro per la semiala sinistra
    
    x2_right = np.array([0, segment_length/2])
    y2_right = np.tan(dihedral_radians_3) * x2_right  # Calcolo della posizione Y con diedro per la semiala destra

    axs[0, 1].plot(x2_left, y2_left, 'k-', linewidth=2)
    axs[0, 1].plot(x2_right, y2_right, 'k-', linewidth=2)
    
    # Vettori di portanza perpendicolari alle semiali con diedro (più piccoli)
    axs[0, 1].quiver(-segment_length/4, y2_left[0] + np.tan(-dihedral_radians_3) * (-segment_length/4), 
               np.sin(dihedral_radians_3) * 3, np.cos(dihedral_radians_3) * 3, angles='xy', scale_units='xy', scale=1, color='g')
    axs[0, 1].quiver(segment_length/4, y2_right[1] + np.tan(dihedral_radians_3) * (segment_length/4), 
               -np.sin(dihedral_radians_3) * 3, np.cos(dihedral_radians_3) * 3, angles='xy', scale_units='xy', scale=1, color='g')
    
    axs[0, 1].set_aspect('equal')
    axs[0, 1].grid(True)
    axs[0, 1].set_xlim(-segment_length, segment_length)
    axs[0, 1].set_ylim(-4, 6)
    axs[0, 1].set_title(f'Segmenti con diedro di {dihedral_angle_3}° e vettori di portanza')
    axs[0, 1].text(-segment_length/4, y2_left[0] + 3.5, 'Portanza Destra', ha='center')
    axs[0, 1].text(segment_length/4, y2_right[1] + 3.5, 'Portanza Sinistra', ha='center')
    axs[0, 1].set_xlabel('Direzione di volo')

    # Segmenti con diedro di 6° per la semiala destra e semiala sinistra orizzontale
    y3_right = np.tan(dihedral_radians_6) * x2_right  # Calcolo della posizione Y con diedro per la semiala destra

    axs[1, 0].plot([-segment_length/2, 0], [0, 0], 'k-', linewidth=2)  # Semiala sinistra orizzontale
    axs[1, 0].plot(x2_right, y3_right, 'k-', linewidth=2)  # Semiala destra inclinata
    
    # Vettori di portanza perpendicolari alle semiali con diedro (più piccoli)
    axs[1, 0].quiver(-segment_length/4, 0, 0, 4, angles='xy', scale_units='xy', scale=1, color='b')
    axs[1, 0].quiver(segment_length/4, y3_right[1] + np.tan(dihedral_radians_6) * (segment_length/4), 
               -np.sin(dihedral_radians_6) * 2, np.cos(dihedral_radians_6) * 2, angles='xy', scale_units='xy', scale=1, color='r')
    
    axs[1, 0].set_aspect('equal')
    axs[1, 0].grid(True)
    axs[1, 0].set_xlim(-segment_length, segment_length)
    axs[1, 0].set_ylim(-4, 6)
    axs[1, 0].set_title(f'Semiala sinistra orizzontale e semiala destra con diedro di {dihedral_angle_6}°')
    axs[1, 0].text(-segment_length/4, 4.5, 'Portanza Destra', ha='center')
    axs[1, 0].text(segment_length/4, y3_right[1] + 2.5, 'Portanza Sinistra', ha='center')
    axs[1, 0].set_xlabel('Direzione di volo')

    # Segmenti con diedro di 3° (uguale al secondo diagramma)
    axs[1, 1].plot(x2_left, y2_left, 'k-', linewidth=2)
    axs[1, 1].plot(x2_right, y2_right, 'k-', linewidth=2)
    
    # Vettori di portanza perpendicolari alle semiali con diedro (più piccoli)
    axs[1, 1].quiver(-segment_length/4, y2_left[0] + np.tan(-dihedral_radians_3) * (-segment_length/4), 
               np.sin(dihedral_radians_3) * 3, np.cos(dihedral_radians_3) * 3, angles='xy', scale_units='xy', scale=1, color='g')
    axs[1, 1].quiver(segment_length/4, y2_right[1] + np.tan(dihedral_radians_3) * (segment_length/4), 
               -np.sin(dihedral_radians_3) * 3, np.cos(dihedral_radians_3) * 3, angles='xy', scale_units='xy', scale=1, color='g')
    
    axs[1, 1].set_aspect('equal')
    axs[1, 1].grid(True)
    axs[1, 1].set_xlim(-segment_length, segment_length)
    axs[1, 1].set_ylim(-4, 6)
    axs[1, 1].set_title(f'Segmenti con diedro di {dihedral_angle_3}° e vettori di portanza (ripetizione)')
    axs[1, 1].text(-segment_length/4, y2_left[0] + 3.5, 'Portanza Destra', ha='center')
    axs[1, 1].text(segment_length/4, y2_right[1] + 3.5, 'Portanza Sinistra', ha='center')
    axs[1, 1].set_xlabel('Direzione di volo')

    plt.show()

# Esecuzione della funzione
plot_wings_with_dihedral_and_lift_vectors_complete_final_adjusted()
