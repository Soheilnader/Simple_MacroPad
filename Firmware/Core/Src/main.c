/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2023 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "ssd1306.h"
#include "fonts.h"
#include "test.h"
#include <stdio.h>
#include "graphics.h"
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
#define R1_PORT GPIOA
#define R1_PIN GPIO_PIN_4

#define R2_PORT GPIOA
#define R2_PIN GPIO_PIN_5

#define R3_PORT GPIOA
#define R3_PIN GPIO_PIN_6

#define R4_PORT GPIOA
#define R4_PIN GPIO_PIN_7

#define C1_PORT GPIOA
#define C1_PIN GPIO_PIN_8

#define C2_PORT GPIOA
#define C2_PIN GPIO_PIN_9

#define C3_PORT GPIOA
#define C3_PIN GPIO_PIN_10
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
I2C_HandleTypeDef hi2c1;

UART_HandleTypeDef huart1;

/* USER CODE BEGIN PV */
uint8_t key, len, row, str[2];
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_I2C1_Init(void);
static void MX_USART1_UART_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
char read_keypad(void);

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_I2C1_Init();
  MX_USART1_UART_Init();
  /* USER CODE BEGIN 2 */
SSD1306_Init (); // initialize the display 

SSD1306_GotoXY (0,0); // goto 10, 10 
SSD1306_Puts ("About Me", &Font_7x10, 1); // print Hello 
SSD1306_GotoXY (0,8); // goto 10, 10 
SSD1306_Puts ("Hello World!", &Font_7x10, 1); // print Hello 
SSD1306_GotoXY (0, 20); 
SSD1306_Puts ("By: Soheil Nadernezhad", &Font_7x10, 1); 
SSD1306_GotoXY (0, 30); 
SSD1306_Puts ("Electronics Engineer", &Font_7x10, 1);
SSD1306_GotoXY (0, 40); 
SSD1306_Puts ("www.soh3il.com", &Font_7x10, 1);
SSD1306_UpdateScreen(); // update screen
HAL_Delay(2000);
SSD1306_Clear();
SSD1306_DrawBitmap(0, 0, gard_logo, 128, 64, 1);
SSD1306_UpdateScreen(); // update screen
HAL_Delay(2000);
SSD1306_Clear();
SSD1306_GotoXY (0,0); // goto 10, 10 

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
    /* USER CODE END WHILE */
key = read_keypad();
if (key != 0)
  {
  SSD1306_Putc(key, &Font_7x10, 1);
  SSD1306_UpdateScreen(); // update screen
  len+=8;
  sprintf(str, "%c", key);
   HAL_UART_Transmit(&huart1, (uint8_t*) str, 1, 10);

  }
if(len >=128)
{
  len = 0;
  row += 10;
SSD1306_GotoXY (0,row); // goto 10, 10 
  
}
    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_NONE;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_HSI;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_0) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief I2C1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_I2C1_Init(void)
{

  /* USER CODE BEGIN I2C1_Init 0 */

  /* USER CODE END I2C1_Init 0 */

  /* USER CODE BEGIN I2C1_Init 1 */

  /* USER CODE END I2C1_Init 1 */
  hi2c1.Instance = I2C1;
  hi2c1.Init.ClockSpeed = 400000;
  hi2c1.Init.DutyCycle = I2C_DUTYCYCLE_2;
  hi2c1.Init.OwnAddress1 = 0;
  hi2c1.Init.AddressingMode = I2C_ADDRESSINGMODE_7BIT;
  hi2c1.Init.DualAddressMode = I2C_DUALADDRESS_DISABLE;
  hi2c1.Init.OwnAddress2 = 0;
  hi2c1.Init.GeneralCallMode = I2C_GENERALCALL_DISABLE;
  hi2c1.Init.NoStretchMode = I2C_NOSTRETCH_DISABLE;
  if (HAL_I2C_Init(&hi2c1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN I2C1_Init 2 */

  /* USER CODE END I2C1_Init 2 */

}

/**
  * @brief USART1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART1_UART_Init(void)
{

  /* USER CODE BEGIN USART1_Init 0 */

  /* USER CODE END USART1_Init 0 */

  /* USER CODE BEGIN USART1_Init 1 */

  /* USER CODE END USART1_Init 1 */
  huart1.Instance = USART1;
  huart1.Init.BaudRate = 9600;
  huart1.Init.WordLength = UART_WORDLENGTH_8B;
  huart1.Init.StopBits = UART_STOPBITS_1;
  huart1.Init.Parity = UART_PARITY_NONE;
  huart1.Init.Mode = UART_MODE_TX_RX;
  huart1.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart1.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART1_Init 2 */

  /* USER CODE END USART1_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOD_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_4|GPIO_PIN_5|GPIO_PIN_6|GPIO_PIN_7, GPIO_PIN_RESET);

  /*Configure GPIO pins : PA4 PA5 PA6 PA7 */
  GPIO_InitStruct.Pin = GPIO_PIN_4|GPIO_PIN_5|GPIO_PIN_6|GPIO_PIN_7;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pins : PA8 PA9 PA10 */
  GPIO_InitStruct.Pin = GPIO_PIN_8|GPIO_PIN_9|GPIO_PIN_10;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

}

/* USER CODE BEGIN 4 */
char read_keypad(void)
{
  HAL_GPIO_WritePin(R1_PORT, R1_PIN, GPIO_PIN_RESET);
  HAL_GPIO_WritePin(R2_PORT, R2_PIN, GPIO_PIN_SET);
  HAL_GPIO_WritePin(R3_PORT, R3_PIN, GPIO_PIN_SET);
  HAL_GPIO_WritePin(R4_PORT, R4_PIN, GPIO_PIN_SET);
  if(HAL_GPIO_ReadPin(C1_PORT, C1_PIN) == 0)
  {
    while(HAL_GPIO_ReadPin(C1_PORT, C1_PIN) == 0);
    return '1';
  }
  if(HAL_GPIO_ReadPin(C2_PORT, C2_PIN) == 0)
  {
    while(HAL_GPIO_ReadPin(C2_PORT, C2_PIN) == 0);
    return '2';
  }
  if(HAL_GPIO_ReadPin(C3_PORT, C3_PIN) == 0)
  {
    while(HAL_GPIO_ReadPin(C3_PORT, C3_PIN) == 0);
    return '3';
  }
  
  HAL_GPIO_WritePin(R1_PORT, R1_PIN, GPIO_PIN_SET);
  HAL_GPIO_WritePin(R2_PORT, R2_PIN, GPIO_PIN_RESET);
  HAL_GPIO_WritePin(R3_PORT, R3_PIN, GPIO_PIN_SET);
  HAL_GPIO_WritePin(R4_PORT, R4_PIN, GPIO_PIN_SET);
  if(HAL_GPIO_ReadPin(C1_PORT, C1_PIN) == 0)
  {
    while(HAL_GPIO_ReadPin(C1_PORT, C1_PIN) == 0);
    return '4';
  }
  if(HAL_GPIO_ReadPin(C2_PORT, C2_PIN) == 0)
  {
    while(HAL_GPIO_ReadPin(C2_PORT, C2_PIN) == 0);
    return '5';
  }
  if(HAL_GPIO_ReadPin(C3_PORT, C3_PIN) == 0)
  {
    while(HAL_GPIO_ReadPin(C3_PORT, C3_PIN) == 0);
    return '6';
  }

  HAL_GPIO_WritePin(R1_PORT, R1_PIN, GPIO_PIN_SET);
  HAL_GPIO_WritePin(R2_PORT, R2_PIN, GPIO_PIN_SET);
  HAL_GPIO_WritePin(R3_PORT, R3_PIN, GPIO_PIN_RESET);
  HAL_GPIO_WritePin(R4_PORT, R4_PIN, GPIO_PIN_SET);
  if(HAL_GPIO_ReadPin(C1_PORT, C1_PIN) == 0)
  {
    while(HAL_GPIO_ReadPin(C1_PORT, C1_PIN) == 0);
    return '7';
  }
  if(HAL_GPIO_ReadPin(C2_PORT, C2_PIN) == 0)
  {
    while(HAL_GPIO_ReadPin(C2_PORT, C2_PIN) == 0);
    return '8';
  }
  if(HAL_GPIO_ReadPin(C3_PORT, C3_PIN) == 0)
  {
    while(HAL_GPIO_ReadPin(C3_PORT, C3_PIN) == 0);
    return '9';
  }

  HAL_GPIO_WritePin(R1_PORT, R1_PIN, GPIO_PIN_SET);
  HAL_GPIO_WritePin(R2_PORT, R2_PIN, GPIO_PIN_SET);
  HAL_GPIO_WritePin(R3_PORT, R3_PIN, GPIO_PIN_SET);
  HAL_GPIO_WritePin(R4_PORT, R4_PIN, GPIO_PIN_RESET);
  if(HAL_GPIO_ReadPin(C1_PORT, C1_PIN) == 0)
  {
    while(HAL_GPIO_ReadPin(C1_PORT, C1_PIN) == 0);
    return 'A';
  }
  if(HAL_GPIO_ReadPin(C2_PORT, C2_PIN) == 0)
  {
    while(HAL_GPIO_ReadPin(C2_PORT, C2_PIN) == 0);
    return '0';
  }
  if(HAL_GPIO_ReadPin(C3_PORT, C3_PIN) == 0)
  {
    while(HAL_GPIO_ReadPin(C3_PORT, C3_PIN) == 0);
    return 'B';
  }
  else
    return 0;
}
/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */